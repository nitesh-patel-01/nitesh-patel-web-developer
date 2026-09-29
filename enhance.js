(()=>{
  const reduced=matchMedia('(prefers-reduced-motion: reduce)');
  const tabs=[...document.querySelectorAll('.stage-tab')];
  const slides=[...document.querySelectorAll('.showcase-slide')];
  let current=0;
  function activate(index,focus=false){
    if(!tabs.length)return;
    current=(index+tabs.length)%tabs.length;
    tabs.forEach((tab,i)=>{let active=i===current;tab.setAttribute('aria-selected',String(active));tab.tabIndex=active?0:-1;slides[i].hidden=!active;slides[i].classList.toggle('active',active)});
    if(focus)tabs[current].focus();
  }
  tabs.forEach((tab,i)=>{tab.addEventListener('click',()=>activate(i));tab.addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key==='ArrowLeft'){e.preventDefault();activate(i+(e.key==='ArrowRight'?1:-1),true)}})});
  document.querySelector('[data-stage-prev]')?.addEventListener('click',()=>activate(current-1));
  document.querySelector('[data-stage-next]')?.addEventListener('click',()=>activate(current+1));
  const form=document.querySelector('#terminal-form');
  const output=document.querySelector('#terminal-output');
  const input=document.querySelector('#terminal-input');
  const responses={
    help:['Available commands: about, projects, skills, surprise, clear','Choose a command above or type one here.'],
    about:['Nitesh Patel · web developer in Jabalpur','I build websites and useful products with a focus on clarity, responsive design and discovery.'],
    projects:['15 projects in the portfolio.','Featured: Hushly, Jabalpur Connect, HappyHealing, John Stamang.','Explore them all at /projects/'],
    skills:['HTML · CSS · JavaScript · PHP · WordPress · WooCommerce','Also: responsive design, REST APIs, performance and technical SEO.'],
    surprise:['You found an easter egg ✦','Every great interface starts with curiosity. Try the projects command next.']
  };
  function run(command){
    if(!output)return;
    const name=command.trim().toLowerCase();
    if(!name)return;
    if(name==='clear'){output.replaceChildren();return}
    const line=document.createElement('p');line.className='terminal-command';line.textContent='$ '+name;output.append(line);
    for(const answer of (responses[name]||['Command not found. Type help for the list.'])){
      const p=document.createElement('p');p.textContent=answer;output.append(p)
    }
    output.scrollTop=output.scrollHeight;
  }
  form?.addEventListener('submit',event=>{event.preventDefault();run(input.value);input.value='';input.focus()});
  document.querySelectorAll('[data-command]').forEach(button=>button.addEventListener('click',()=>{run(button.dataset.command);input?.focus()}));
  const briefType=document.querySelector('#brief-type');
  const briefGoal=document.querySelector('#brief-goal');
  if(briefType&&briefGoal){
    const types={business:['Business website','clear services, trust signals and a direct contact route'],product:['Web product','a guided first-use journey and helpful interface states'],store:['Online store','useful product detail and a straightforward checkout path'],portfolio:['Portfolio','selected work with context and an easy enquiry path']};
    const goals={enquiries:['More useful enquiries','Map visitor questions','Connect relevant pages to contact'],clarity:['Explain the offer clearly','Put the core offer first','Use plain navigation and concrete examples'],sales:['Support sales','Show product or service detail','Reduce uncertainty before the decision'],speed:['Improve site speed','Audit the current page weight','Prioritize content and essential scripts']};
    function renderBrief(){
      const [title,description]=types[briefType.value], [goal,first,second]=goals[briefGoal.value];
      const code=`const project = {\n  type: '${briefType.value}',\n  priority: '${briefGoal.value}',\n  delivery: 'responsive + accessible'\n};\n\nbuild(project);`;
      document.querySelector('#brief-code').textContent=code;
      document.querySelector('#brief-title').textContent=title+' → '+goal;
      document.querySelector('#brief-summary').textContent='Start with '+description+'.';
      document.querySelector('#brief-steps').textContent='01 / '+first+'   ·   02 / '+second+'   ·   03 / Test and refine';
      return `${title} — ${goal}\n${description}.\nFirst steps: ${first}; ${second}; test and refine.`;
    }
    briefType.addEventListener('change',renderBrief);briefGoal.addEventListener('change',renderBrief);renderBrief();
    document.querySelector('#brief-copy').addEventListener('click',async()=>{
      try{await navigator.clipboard.writeText(renderBrief());document.querySelector('#brief-status').textContent='Brief copied. Paste it into your message.'}
      catch{document.querySelector('#brief-status').textContent='Clipboard unavailable. You can select the plan from the preview.'}
    });
  }
  const meter=document.querySelector('.scroll-meter');
  let scrolling=false;
  function updateScroll(){
    scrolling=false;
    if(meter){
      const max=document.documentElement.scrollHeight-innerHeight;
      meter.style.transform=`scaleX(${max>0?Math.min(1,scrollY/max):0})`;
    }
  }
  addEventListener('scroll',()=>{if(!scrolling){scrolling=true;requestAnimationFrame(updateScroll)}},{passive:true});
  updateScroll();
  if(!reduced.matches&&'IntersectionObserver' in window){
    const items=document.querySelectorAll('section h2, section h3, .page-intro h1, .area-code span');
    const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{
      if(entry.isIntersecting){entry.target.classList.add('motion-shown');observer.unobserve(entry.target)}
    }),{threshold:.12,rootMargin:'0px 0px -25px 0px'});
    items.forEach(item=>{item.classList.add('motion-step');observer.observe(item)});
  }
  const palette=document.querySelector('.quick-palette');
  const paletteInput=document.querySelector('#palette-input');
  const paletteResults=document.querySelector('.palette-results');
  const routes=new Map();
  document.querySelectorAll('a[href^="/"]').forEach(link=>{
    const href=link.getAttribute('href');
    if(!href||href.includes('#')||routes.has(href))return;
    let title=link.querySelector('h3')?.textContent||link.textContent.trim();
    title=title.replace(/\s+/g,' ').trim();
    if(title)routes.set(href,title.slice(0,80));
  });
  for(const [href,title] of [['/','Home'],['/projects/','All projects'],['/web-developer/','Service areas'],['/contact/','Contact Nitesh']])routes.set(href,title);
  function renderRoutes(){
    if(!paletteResults)return;
    const term=paletteInput.value.trim().toLowerCase();
    paletteResults.replaceChildren();
    let count=0;
    for(const [href,title] of routes){
      if(term&&!`${title} ${href}`.toLowerCase().includes(term))continue;
      const a=document.createElement('a');a.href=href;
      const strong=document.createElement('strong');strong.textContent=title;
      const small=document.createElement('small');small.textContent=href;
      a.append(strong,small);paletteResults.append(a);
      if(++count>=8)break;
    }
    if(!count){const p=document.createElement('p');p.textContent='No matching page. Try a project or service name.';paletteResults.append(p)}
  }
  let routesLoaded=false;
  function openPalette(){
    if(!palette||palette.open)return;
    palette.showModal();paletteInput.value='';renderRoutes();paletteInput.focus();
    if(!routesLoaded){
      fetch('/routes.json').then(response=>response.ok?response.json():[]).then(list=>{
        if(!Array.isArray(list))return;
        list.forEach(([href,title])=>routes.set(href,title));
        routesLoaded=true;renderRoutes();
      }).catch(()=>{});
    }
  }
  document.querySelector('.palette-launch')?.addEventListener('click',openPalette);
  paletteInput?.addEventListener('input',renderRoutes);
  addEventListener('keydown',event=>{
    const editing=event.target.matches?.('input,textarea,select,[contenteditable]');
    if((event.key.toLowerCase()==='k'&&(event.metaKey||event.ctrlKey))||(event.key==='/'&&!editing)){
      event.preventDefault();openPalette();
    }
  });
})();

/* Shared contact shortcuts on every page. */
(() => {
  const style = document.createElement('style');
  style.textContent = '.contact-float{position:fixed;right:max(16px,env(safe-area-inset-right));bottom:calc(20px + env(safe-area-inset-bottom));z-index:90;display:flex;flex-direction:column;gap:10px}.contact-float a{display:grid;place-items:center;width:52px;height:52px;border-radius:50%;color:#fff;border:1px solid #ffffff40;box-shadow:0 6px 20px #0005;transition:transform .2s;text-decoration:none}.contact-float a:hover{transform:translateY(-3px)}.contact-float a:focus-visible{outline:3px solid #fff;outline-offset:4px}.contact-float .contact-call{background:#2563eb}.contact-float .contact-whatsapp{background:#128c4a}.contact-float svg{width:25px;height:25px}@media(prefers-reduced-motion:reduce){.contact-float a{transition:none}}';
  document.head.append(style);
  const shortcuts = document.createElement('nav');
  shortcuts.className = 'contact-float';
  shortcuts.setAttribute('aria-label', 'Contact Nitesh');
  const message = 'Hi Nitesh! I found you through your portfolio website and would like to discuss a website project.\nPage: ' + location.origin + location.pathname;
  shortcuts.innerHTML = '<a class="contact-call" href="tel:+917974823298" aria-label="Call Nitesh about a website project" title="Call Nitesh"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.5 2.1L8 10a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.9.6 2.9.7a2 2 0 0 1 1.7 2z"/></svg></a><a class="contact-whatsapp" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp Nitesh about a website project" title="Discuss your website on WhatsApp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M20.5 11.5a8.5 8.5 0 0 1-12.6 7.4L3 20.5l1.6-4.9a8.5 8.5 0 1 1 15.9-4.1z"/><path d="M8 7.5c-.6 1-.1 3 1.6 4.7s3.7 2.2 4.7 1.6l1-1-2-1-1 1c-1.3-.5-2.6-1.8-3.1-3.1l1-1-1-2z"/></svg></a>';
  shortcuts.querySelector('.contact-whatsapp').href = 'https://wa.me/917974823298?text=' + encodeURIComponent(message);
  document.body.append(shortcuts);
})();
