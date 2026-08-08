"""Patch the downloaded book-theme template: replace the dialog-based
search with a flat top-bar input, and add the organizing-body logos to
the bottom of the sidebar.

Ported from the nanobeam-course site. The stock theme's search opens a
modal dialog and there is no template option to change it, so we patch
the compiled bundles in _build/templates. Run after the template has been
downloaded (any `myst build` or `myst start` does that), and re-run
whenever _build is cleared:

    python3 scripts/patch_theme.py

The deploy workflow runs this between a warm-up build and the real build.
"""

import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.normpath(
    os.path.join(HERE, "..", "_build", "templates", "site", "myst", "book-theme")
)


# Flat top-bar search runtime (replaces the theme's dialog search).
# Injected into the server-rendered HTML. The search index path is
# resolved relative to the current page so it also works when the site
# is served under a path prefix (GitHub Pages project sites).
_RUNTIME = """
;(function(){
  /* ---------- flat top-bar search (replaces the theme's dialog) -------- */
  var idx=null,loading=false,waiters=[];
  function indexUrls(){
    var seg=window.location.pathname.split('/').filter(Boolean);
    var urls=['/myst.search.json'];
    if(seg.length)urls.unshift('/'+seg[0]+'/myst.search.json');
    return urls;
  }
  function load(cb){
    if(cb&&idx)return cb();
    if(cb)waiters.push(cb);
    if(idx||loading)return;
    loading=true;
    var urls=indexUrls();
    function attempt(i){
      if(i>=urls.length){loading=false;waiters=[];return;}
      fetch(urls[i]).then(function(r){
        if(!r.ok)throw new Error('http '+r.status);
        return r.json();
      }).then(function(d){
        idx=d.records||[];loading=false;
        var w=waiters;waiters=[];w.forEach(function(f){f();});
      }).catch(function(){attempt(i+1);});
    }
    attempt(0);
  }
  function titleOf(h){
    return [h.lvl3,h.lvl2,h.lvl1].filter(Boolean)[0]||'';
  }
  function crumbOf(h){
    return [h.lvl1,h.lvl2,h.lvl3].filter(Boolean).join(' > ');
  }
  function search(q){
    if(!idx)return [];
    var terms=q.toLowerCase().split(/\\s+/).filter(Boolean);
    if(!terms.length)return [];
    var seen={},out=[];
    idx.forEach(function(rec){
      var h=rec.hierarchy||{};
      var title=titleOf(h),crumb=crumbOf(h);
      var hay=(crumb+' '+(rec.content||'')).toLowerCase();
      var titleHay=crumb.toLowerCase();
      var score=0;
      for(var i=0;i<terms.length;i++){
        if(hay.indexOf(terms[i])<0)return;
        if(titleHay.indexOf(terms[i])>=0)score+=3;
        score+=1;
      }
      if(rec.type!=='content')score+=2;
      var key=rec.url;
      if(seen[key]!==undefined){
        if(out[seen[key]].score>=score)return;
        out[seen[key]]={score:score,url:rec.url,title:title,crumb:crumb,
                        content:rec.content||''};
        return;
      }
      seen[key]=out.length;
      out.push({score:score,url:rec.url,title:title,crumb:crumb,
                content:rec.content||''});
    });
    out.sort(function(a,b){return b.score-a.score;});
    return out.slice(0,8);
  }
  function build(bar){
    if(!bar||bar.dataset.ecsSearch)return;
    bar.dataset.ecsSearch='1';
    var wrap=document.createElement('div');
    wrap.className='ecs-search';
    var input=document.createElement('input');
    input.type='search';
    input.placeholder='Search';
    input.setAttribute('aria-label','Search this site');
    var list=document.createElement('div');
    list.className='ecs-search-results';
    list.hidden=true;
    wrap.appendChild(input);
    wrap.appendChild(list);
    bar.style.display='none';
    bar.after(wrap);
    var active=-1,hits=[];
    function render(){
      list.innerHTML='';
      if(!hits.length){list.hidden=true;return;}
      hits.forEach(function(h,i){
        var a=document.createElement('a');
        a.href=h.url;
        a.className='ecs-search-hit'+(i===active?' active':'');
        var t=document.createElement('div');
        t.className='ecs-search-hit-title';
        t.textContent=h.crumb||h.title;
        a.appendChild(t);
        if(h.content){
          var c=document.createElement('div');
          c.className='ecs-search-hit-text';
          c.textContent=h.content.slice(0,110);
          a.appendChild(c);
        }
        list.appendChild(a);
      });
      list.hidden=false;
    }
    function run(){
      active=-1;
      hits=search(input.value.trim());
      render();
    }
    input.addEventListener('focus',function(){load();});
    input.addEventListener('input',function(){
      load(run);   // re-runs once the index finishes loading
      run();
    });
    input.addEventListener('keydown',function(ev){
      if(ev.key==='ArrowDown'||ev.key==='ArrowUp'){
        ev.preventDefault();
        if(!hits.length)return;
        active=(active+(ev.key==='ArrowDown'?1:-1)+hits.length)%hits.length;
        render();
      }else if(ev.key==='Enter'){
        var h=hits[active<0?0:active];
        if(h){ev.preventDefault();window.location.href=h.url;}
      }else if(ev.key==='Escape'){
        input.value='';hits=[];render();input.blur();
      }
    });
    document.addEventListener('click',function(ev){
      if(!wrap.contains(ev.target)){hits=[];render();}
    });
    document.addEventListener('keydown',function(ev){
      if((ev.metaKey||ev.ctrlKey)&&ev.key.toLowerCase()==='k'){
        ev.preventDefault();ev.stopPropagation();input.focus();input.select();
      }
    },true);
  }
  /* ---------- organizing-body logos at the bottom of the sidebar ------- */
  var ORGS=[['International Union of Crystallography','https://www.iucr.org/','__IUCR__'],
            ['European Crystallographic Association','https://www.ecanews.org/','__ECA__'],
            ['ELECTRA','https://electraec.wordpress.com/','__ELECTRA__']];
  function orgsTick(){
    var toc=document.querySelector('.myst-primary-sidebar-toc');
    if(!toc||!toc.parentElement)return;
    if(toc.parentElement.querySelector('.ecs-org-logos'))return;
    var box=document.createElement('div');
    box.className='ecs-org-logos';
    ORGS.forEach(function(o){
      var a=document.createElement('a');
      a.href=o[1];a.target='_blank';a.rel='noopener';a.title=o[0];
      var img=document.createElement('img');
      img.alt=o[0];img.src=o[2];
      a.appendChild(img);
      box.appendChild(a);
    });
    toc.after(box);
  }

  function tick(){
    build(document.querySelector('button.myst-search-bar'));
    orgsTick();
  }
  function start(){
    tick();
    // React hydration replaces these nodes, so keep re-checking for a while
    var n=0,iv=setInterval(function(){tick();if(++n>40)clearInterval(iv);},250);
    new MutationObserver(function(){tick();}).observe(
      document.documentElement,{subtree:true,childList:true});
  }
  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded',start);
  }else{start();}
})();
"""

def _data_uri(path):
    import base64
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


LOGOS = os.path.normpath(os.path.join(HERE, "..", "assets", "logos"))
for token, filename in [
    ("__IUCR__", "iucr.png"),
    ("__ECA__", "eca.png"),
    ("__ELECTRA__", "electra.png"),
]:
    _RUNTIME = _RUNTIME.replace(token, _data_uri(os.path.join(LOGOS, filename)))

# The marker embeds a hash of the runtime, so editing the code above is
# enough to make the next patch run replace an older injected copy.
INLINER_MARK = (
    "/*ecs-runtime-" + hashlib.sha1(_RUNTIME.encode()).hexdigest()[:8] + "*/"
)
INLINER = INLINER_MARK + _RUNTIME




def main():
    if not os.path.isdir(THEME):
        sys.exit("book-theme template not found; run `myst build` first")
    total = 0
    # dev server: drop the 1-year immutable cache so patched bundles reload
    server_js = os.path.join(THEME, "server.js")
    if os.path.exists(server_js):
        with open(server_js) as f:
            ssrc = f.read()
        fixed = ssrc.replace(
            "{ immutable: true, maxAge: '1y' }", "{ maxAge: '5m' }"
        )
        if fixed != ssrc:
            with open(server_js, "w") as f:
                f.write(fixed)
            print("patched server.js (cache headers)")
    # inject the search runtime into the server-rendered HTML itself; the
    # document is never long-cached, unlike the fingerprinted JS bundles
    import json
    server_bundle = os.path.join(THEME, "build", "index.js")
    with open(server_bundle) as f:
        bsrc = f.read()
    tag = json.dumps("<script>" + INLINER + "</script></body>")
    if INLINER_MARK in bsrc:
        print("already patched: build/index.js (search runtime)")
    elif "ecs-runtime" in bsrc:  # older runtime: swap it out
        new_bsrc, n = re.subn(
            r'"<script>[^"]*ecs-runtime[^"]*</script></body>"',
            lambda m: tag,
            bsrc,
        )
        with open(server_bundle, "w") as f:
            f.write(new_bsrc)
        total += n
        print(f"updated build/index.js runtime ({n} site)")
    else:
        new_bsrc, n = re.subn(
            r'new Response\("<!DOCTYPE html>"\+(\w+),',
            lambda m: (
                'new Response("<!DOCTYPE html>"+'
                f'{m.group(1)}.replace("</body>",{tag}),'
            ),
            bsrc,
        )
        if n == 0:
            sys.exit("SSR injection point not found; theme version changed?")
        with open(server_bundle, "w") as f:
            f.write(new_bsrc)
        total += n
        print(f"patched build/index.js (search runtime, {n} site)")
    # rename the patched entry + manifest so browsers that cached the stock
    # bundles (1-year immutable) fetch the patched versions
    rename = [("entry.client-PCJPW7TK", "entry.client-ECSRT1"),
              ("manifest-C732C875", "manifest-ECSRT1")]
    pub = os.path.join(THEME, "public", "build")
    if not os.path.exists(os.path.join(pub, "entry.client-ECSRT1.js")):
        import shutil
        for old, new in rename:
            shutil.copyfile(
                os.path.join(pub, f"{old}.js"), os.path.join(pub, f"{new}.js")
            )
        for path in [os.path.join(THEME, "build", "index.js")] + [
            os.path.join(pub, "manifest-ECSRT1.js")
        ]:
            with open(path) as f:
                s = f.read()
            for old, new in rename:
                s = s.replace(old, new)
            with open(path, "w") as f:
                f.write(s)
        print("renamed entry.client + manifest (cache bust)")

    print(f"done ({total} replacements)")


if __name__ == "__main__":
    main()
