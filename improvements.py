from sales import offers, business_proof, reassurance
from html import escape as e

def category(slug):
 return 'business' if slug in ['happyhealing','ak-goud-properties','shri-dadaji'] else 'apps' if slug in ['hushly','jabalpur-connect','fitcoach','dhanda-tycoon','zen-flow-henna'] else 'tools'

playground='''<section class="design-lab"><div class="wrap"><div class="lab-heading"><div><span class="eyebrow">MAKE A SMALL CHANGE. SEE THE DIFFERENCE.</span><h2>Your turn to build.</h2></div><p>Change the layout and accent. The preview and CSS update together.</p></div><div class="lab-grid"><div class="lab-editor"><div class="lab-controls"><label>Layout <select id="demo-layout"><option value="row">Side by side</option><option value="column">Stacked</option></select></label><label>Accent <select id="demo-accent"><option value="#81f5ee">Mint</option><option value="#ffd18a">Amber</option><option value="#8abaff">Blue</option></select></label></div><pre id="demo-code">.preview-card {
  display: flex;
  flex-direction: row;
  --accent: #81f5ee;
}</pre></div><div class="demo-preview" id="demo-preview"><div class="demo-art" aria-hidden="true">&lt;/&gt;</div><div><small>LIVE / YOUR CREATION</small><h3>A clear idea.<br>A useful website.</h3><p>Design is a series of choices. Try a different one.</p><a href="/contact/">Build something together ↗</a></div></div></div></div></section>'''

article_sections={
'website-cost-india':[
('The short answer: scope determines the quote','A website quote should name what will be delivered, who supplies content and what happens after launch. A five-page brochure site and a store with payments, delivery rules and hundreds of products require different work. Without that scope, two prices are difficult to compare.'),
('Write a page and feature inventory','List the homepage, service pages, about page, contact page and any articles or location pages you actually need. Beside each page, write the visitor action: call, ask for an estimate, read a guide or buy a product. Record integrations separately, such as WhatsApp enquiries, a booking tool, a CMS or payment processing.'),
('Separate one-time and recurring costs','Design, development, content entry and migration are usually project tasks. Domains, hosting, paid plugins, email services and maintenance can recur. Ask which subscriptions are purchased in your name and how you will regain access if the developer changes. Also clarify whether additional revisions and future content changes are included.'),
('Compare acceptance criteria','A useful agreement identifies supported screen sizes, working enquiry flows, content supplied, URL redirects where necessary, metadata, handover and a review period. For a redesign, ask whether existing URLs and important search pages will be preserved. For a store, specify how checkout and failed payments will be reviewed.'),
('Send a brief that makes estimates useful','Send your existing URL, five examples of required pages, the main customer action, editing needs and your target launch window. Mark content as ready, needs editing or not yet written. That short list is more useful than asking for a price for an undefined “professional website.”')],
'wordpress-vs-custom':[
('Choose around editing and functionality','WordPress suits sites whose owners regularly publish pages, articles or products. A custom build can suit a focused interface or a workflow that does not fit a conventional CMS. Neither choice automatically makes a site fast, secure or easier to use; implementation and maintenance determine much of that outcome.'),
('When WordPress is a practical fit','A business with several service pages, a blog and a team that edits copy may benefit from an established dashboard. WooCommerce can support an editable catalog and store operations. Define editor roles, required plugins, backups and update responsibilities before committing to the platform.'),
('When a custom build makes sense','A small static portfolio can serve content without a CMS database. Interactive tools can use custom interfaces for calculations, previews and specialized inputs. If you still need editing, budget for a content workflow or a CMS integration; “custom” should not mean that every sentence requires a developer.'),
('Ask who will maintain it','For WordPress, review plugin necessity, licensing, updates and restore procedures. For custom code, ask about repository access, build instructions, deployment and dependency updates. In both cases, ensure the business owns its hosting, domain and account access.'),
('Make the decision with a real task','Ask the developer to demonstrate a common task: changing a service description, adding a product or publishing a guide. Then compare the time, skills and ongoing costs required. Choose the platform whose workflow your team can realistically maintain.')],
'mobile-first-design-checklist':[
('Start with the enquiry journey','Open the homepage on a narrow phone screen and explain the offer in one sentence. The introduction should lead naturally to the relevant service or project and then to contact. Navigation should work with a thumb and should not hide behind decorative animation.'),
('Find the source of sideways scrolling','Test long headings, code blocks, tables, form controls and grid children. Flexible children often need min-width: 0; code can use white-space: pre-wrap and overflow-wrap: anywhere. Avoid fixing every problem with a global overflow rule that simply hides inaccessible content.'),
('Make contact controls useful','Phone and WhatsApp buttons need descriptive labels and should leave space for page content and device safe areas. Check that the WhatsApp message identifies the enquiry context without collecting unnecessary information. Fill the form with realistic long values and verify validation messages remain visible.'),
('Review text and keyboard behavior','Increase text size, tab through controls and check focus indicators. Inputs need visible labels rather than placeholders alone. Dropdowns and dialogs should open, close and return focus predictably. Relevant content should remain available when motion is reduced or JavaScript fails.'),
('Check the whole site, not just the hero','Review a project detail, service page, article, location page and contact form at 320, 375 and 430 pixels wide. Test portrait and landscape. Images should have reserved dimensions, readable captions and sensible crop behavior.')],
'seo-ready-launch':[
('Make important pages reachable','Each important service, project and article needs a normal internal link and a successful page response. Check the navigation and useful contextual links. A sitemap can assist discovery, but it does not replace a site structure that visitors can follow.'),
('Give each page a clear identity','Write a unique title and description that describe the actual page. Use one clear H1 and logical subheadings. Canonical URLs should use the public production domain consistently. Verify that social images are publicly accessible and the Open Graph description matches the page.'),
('Publish accurate structured data','Person data should describe the actual developer. Article data should match visible authorship and dates. Breadcrumbs should reflect the page hierarchy. Do not add ratings, local offices or results that are not supported by the visible content.'),
('Check crawler files and redirects','The sitemap should list canonical indexable pages, excluding redirects and duplicates. robots.txt should point to it. Keep private information behind authentication rather than relying on crawler instructions. When migrating a domain, plan redirects from important old URLs.'),
('Measure after launch','Verify Search Console ownership, submit the sitemap and inspect important URLs. Review indexing explanations, search queries and enquiry quality over time. Do not treat a verification tag or an optional llms.txt file as proof that pages are indexed or rankings have improved.')],
'local-seo-jabalpur':[
('Describe the actual service area','State that the business is based in Jabalpur and explain whether services are delivered remotely or in person. A page for Mumbai should not imply a Mumbai office if there is none. Accurate contact information and a realistic service description make the offer easier to evaluate.'),
('Use location pages to answer distinct questions','A useful area page explains a real audience, service need, process and enquiry route. Changing only a city name produces little new value. Before publishing another page, identify what decision it helps the visitor make and which evidence or example supports it.'),
('Connect services, proof and contact','Link the page to the most relevant service and a project illustrating the workflow. A shop may need product categories and direct contact; an institute may need admissions information and document guidance. Keep business hours and addresses accurate when they apply.'),
('Build legitimate business signals','If the business qualifies for a Google Business Profile, maintain accurate category, service areas and contact details. Ask real clients for honest feedback without inventing testimonials. Keep professional profiles consistent and link to work that demonstrates your experience.'),
('Review actual search demand','Use Search Console to discover the queries and pages that receive impressions. Improve the information on useful pages before expanding to dozens more cities. Location pages on your own domain are internal content; they are not external backlinks.')]
}

def enrich(path,body,title):
 if path=='/':
  body=body.replace('<section class="design-lab">',offers()+business_proof()+'<section class="design-lab">',1)
  body=body.replace('<section id="whatsapp-enquiry"',reassurance()+'<section id="whatsapp-enquiry"',1)
 if path.startswith('/projects/') and path!='/projects/':
  slug=path.strip('/').split('/')[-1]
  evidence={
   'ak-goud-properties':('Help property buyers understand the offer before making contact.','The live site presents plots, villas and apartments, Hyderabad service locations and the site-visit process.','Service sections connect to a direct WhatsApp enquiry route.'),
   'shri-dadaji':('Make a local agricultural shop easier to find and enquire about.','The live storefront introduces product categories and shop information in a bilingual interface.','Visitors can move from the product overview to phone or WhatsApp contact.'),
   'happyhealing':('Present a handloom catalog with a usable shopping route.','The live site includes saree categories, individual product pages and a shopping interface.','Visitors can inspect product presentation and follow the collection into the store.'),
   'hushly':('Make a shared question link understandable to a social visitor.','The live homepage explains the question and sharing workflow and offers an account entry point.','The interface provides a clear route to begin; account-only features require signing in.'),
   'invoice-generator':('Keep invoice information and document preview close together.','The live interface includes business details, invoice fields and a document preview.','The export and print controls are visible alongside the form; financial outcomes are not measured here.')
  }
  if slug in evidence:
   goal,interface,delivered=evidence[slug]
   body+='<section><div class="wrap"><span class="eyebrow">CASE STUDY / VISIBLE PROJECT EVIDENCE</span><h2>From visitor need to working interface.</h2><div class="detail-grid">'+''.join('<article class="detail"><h3>'+e(h)+'</h3><p>'+e(p)+'</p></article>' for h,p in [('The visitor need',goal),('The interface',interface),('The delivered experience',delivered)])+'</div><p class="small">Explore the live project to review the experience. Traffic, revenue and conversion improvements are not claimed without supporting analytics.</p></div></section>'
 if path.startswith('/projects/') and path!='/projects/':
  body+='<section><div class="wrap related-work"><span class="eyebrow">HAVE A SIMILAR PROJECT?</span><h2>Let’s build a website for your business.</h2><p class="lead">Tell me about your audience and what visitors should do. We can turn that into a website brief and an agreed quote.</p><a class="button" href="/hire-web-developer/#quote-form">Request a website quote ↗</a></div></section>'
 if path!='/':
  label=path.strip('/').split('/')[0]
  body='<nav class="wrap breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span>/</span> '+(f'<a href="/{label}/">{e(label.replace("-"," ").title())}</a> <span>/</span> ' if path.count('/')>2 else '')+f'<span>{e(title.split(" — ")[0])}</span></nav>'+body
 if path=='/projects/':
  filters='<div class="filterbar" aria-label="Filter projects">'+''.join(f'<button type="button" data-project-filter="{key}" aria-pressed="{str(key=="all").lower()}">{label}</button>' for key,label in [('all','All projects'),('business','Business websites'),('apps','Web apps'),('tools','Useful tools')])+'</div><p id="project-count" role="status"></p>'
  body=body.replace('<div class="grid">',filters+'<div class="grid">',1)
 if path.startswith('/services/') and path!='/services/':
  slug=path.strip('/').split('/')[-1]
  scope={
   'wordpress-development':[('Editable content','Set up an editing workflow for agreed pages, posts or products.'),('A maintainable setup','Select necessary plugins, document licenses and agree who handles backups and updates.'),('Handover','Review common editing tasks and provide the agreed access and project files.')],
   'landing-pages':[('One campaign goal','Define the audience, offer, objections and main action before the layout.'),('Useful evidence','Use real work, product details and approved testimonials where available.'),('A complete enquiry route','Connect the CTA to a form or contact method and review the mobile journey.')],
   'seo-performance':[('Technical review','Check indexability, canonical URLs, internal links, metadata and image handling.'),('Focused fixes','Prioritize issues that block content or slow the most important pages.'),('Measurement plan','Compare before and after lab results and review real search data when access is available.')]
  }.get(slug,[('Content and structure','Agree on pages, visitor questions and the primary action for each page.'),('Responsive build','Review real text, images, navigation and contact controls across screen sizes.'),('Launch and handover','Check links, metadata and forms, then agree access, ownership and support responsibilities.')])
  body+='<section><div class="wrap"><span class="eyebrow">DELIVERABLES / AGREED BEFORE BUILDING</span><h2>Know what the work includes.</h2><div class="detail-grid">'+''.join(f'<article class="detail"><h3>{e(a)}</h3><p>{e(b)}</p></article>' for a,b in scope)+'</div><div class="callout"><h3>What happens after launch?</h3><p>We agree a review period, the changes it covers, and an optional maintenance scope. Domain, hosting, paid software and ongoing content work are listed separately where applicable. You should know who owns the accounts and how to request a change.</p><a href="/writing/website-cost-india/">How to compare website quotes ↗</a> · <a href="/writing/wordpress-vs-custom/">Choose the right platform ↗</a></div></div></section>'
 if path.startswith('/writing/') and path!='/writing/':
  slug=path.strip('/').split('/')[-1]
  if slug in article_sections:
   start=body.index('<section><article')
   body=body[:start]+'<section><article class="wrap article"><p class="meta">By Nitesh Patel · Updated 30 September 2026</p>'+''.join(f'<h2>{e(h)}</h2><p>{e(p)}</p>' for h,p in article_sections[slug])+'<div class="callout"><h3>Your next step</h3><p>Write down your site’s main visitor task and review the page that supports it. Bring that page and your questions to a first conversation.</p><a href="/contact/">Discuss your website ↗</a></div></article></section>'
  body+='<section><div class="wrap article"><h2>Continue reading</h2><ul>'+''.join(f'<li><a href="/writing/{s}/">{e(article_sections[s][0][0])}</a></li>' for s in ['website-cost-india','wordpress-vs-custom','mobile-first-design-checklist'] if s!=slug)+'</ul><a href="/services/">Explore development services ↗</a></div></section>'
 if path.startswith('/web-developer/') and path.count('/')>=3:
  body+='<section><div class="wrap"><span class="eyebrow">FROM PLAN TO INTERFACE</span><h2>A useful reference for your brief.</h2><div class="detail-grid"><article class="detail"><h3>Local shop or service</h3><p>Look at Shri Dadaji for a product-category and direct-contact approach.</p><a href="/projects/shri-dadaji/">See the storefront ↗</a></article><article class="detail"><h3>Interactive application</h3><p>Explore how a focused task becomes a browser interface in the invoice tool.</p><a href="/projects/invoice-generator/">See the invoice tool ↗</a></article><article class="detail"><h3>Before asking for a quote</h3><p>Prepare the page list, required features, content status and editing needs.</p><a href="/writing/website-cost-india/">Read the scoping guide ↗</a></article></div></div></section>'
 return body

