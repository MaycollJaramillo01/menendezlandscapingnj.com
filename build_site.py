from pathlib import Path
from html import escape
import json
import shutil
from datetime import date

ROOT = Path(__file__).parent
OUT = ROOT / "public"
SITE = "https://menendezlandscapingnj.com"
PHONE = "(609) 516-6584"
PHONE_HREF = "+16095166584"
EMAIL = "info@menendezlandscapingnj.com"
WHATSAPP = "https://wa.me/16095166584?text=Hello%20Menendez%20Landscaping%2C%20I%27d%20like%20a%20free%20estimate."
SOCIAL_LINKS = [
    ("Google Business Profile", "https://maps.app.goo.gl/GyWREQJ3ytXg93kK9?g_st=awb"),
    ("Facebook", "https://www.facebook.com/share/1JGsLMpETj/"),
    ("Instagram", "https://www.instagram.com/menendezlandscaping/"),
    ("TikTok", "https://www.tiktok.com/t/ZTyg3cQAM/"),
]

MEDIA = {
    "hero-patio.jpeg": "a37b7802-1d73-4de1-a865-601f1908b79e.jpeg",
    "landscaping.jpeg": "c109fd05-690a-417d-84dc-6e78040405fc (1).jpeg",
    "mulching.jpeg": "63e84998-8502-46ec-b077-c8050f4ec100.jpeg",
    "pruning.jpeg": "bf427b68-0832-4813-82eb-ba1afd5dd3a2.jpeg",
    "planting.jpeg": "574efbb2-026d-4224-ad21-6bcaa675a951.jpeg",
    "renovation.jpeg": "62c01748-cf64-4f90-88e5-67972b72c12d (1).jpeg",
    "walkways.jpeg": "ed4d9583-e503-4555-aa20-dde7b3e83746 (1).jpeg",
    "patios.jpeg": "e8e6ef3b-95a4-4cd5-b6eb-e5551d6a449a.jpeg",
    "stonework.jpeg": "0b84489b-23af-4010-b42b-6c569aefe995 (1).jpeg",
    "power-washing.jpeg": "b0d54ba9-a1a3-4dc9-8b6e-f0cbc194006b.jpeg",
    "kitchen.jpeg": "bf1be795-5f8a-423a-ac38-c0d396c16958.jpeg",
    "flooring.jpeg": "1511f050-2cc6-4087-9ff9-ca9390df605b.jpeg",
    "bathroom.jpeg": "d8d4e231-8534-4c35-9295-55861e57088b.jpeg",
    "painting.jpeg": "f35203b4-d17f-46ab-b142-94e04a0b73da.jpeg",
    "garden.jpeg": "b93a463d-1b38-4ce9-bfa5-bb578931f37f.jpeg",
    "lawn.jpeg": "b867b5fc-32d7-443a-913e-ef732670edbe (1).jpeg",
    "brand-mark.png": None,
}

GROUPS = [
    {"id": "landscaping", "name": "Landscaping", "image": "landscaping.jpeg", "alt": "Lawn, garden beds and stone landscape edging", "intro": "Design, installation and care for garden and outdoor spaces."},
    {"id": "hardscaping", "name": "Hardscaping", "image": "hero-patio.jpeg", "alt": "Paver patio and outdoor living area", "intro": "Patios, walkways, stonework and power washing."},
    {"id": "remodeling", "name": "Home remodeling", "image": "kitchen.jpeg", "alt": "Kitchen remodeling work in progress", "intro": "Kitchen, bathroom, flooring and painting projects."},
]

SERVICES = [
    {"id":"landscaping","group":"Landscaping","name":"Landscaping","seo":"Landscaping Design & Installation","headline":"A landscape that fits your property.","summary":"Design, installation and maintenance for gardens and outdoor spaces.","body":"Plan and install outdoor spaces around your property, from garden areas to broader landscape updates. Menendez Landscaping also provides maintenance for residential and commercial customers.","points":["Landscape planning and layout","Garden and outdoor-area installation","Maintenance suited to the property"],"image":"landscaping.jpeg","alt":"Residential landscape with lawn, planting beds and stone edging"},
    {"id":"mulching","group":"Landscaping","name":"Mulching","seo":"Mulching Service","headline":"A clean finish for garden beds.","summary":"Mulch application to help protect soil, retain moisture and refresh beds.","body":"Fresh mulch can give planting beds a tidy finish while helping the soil retain moisture. Application and coverage are planned around the condition and layout of each bed.","points":["Refresh existing planting beds","Help protect soil and conserve moisture","Finish bed edges for a neat appearance"],"image":"mulching.jpeg","alt":"Garden bed with ornamental plants and fresh mulch"},
    {"id":"pruning","group":"Landscaping","name":"Pruning","seo":"Tree & Shrub Pruning","headline":"Keep plants shaped and cared for.","summary":"Pruning and maintenance for trees, shrubs and other vegetation.","body":"Pruning helps keep trees, shrubs and other plants neat and aligned with the surrounding landscape. Each project is scoped around the vegetation on site and the work requested.","points":["Tree and shrub pruning","Vegetation maintenance","A finish that works with surrounding beds"],"image":"pruning.jpeg","alt":"Established shrubs and colorful landscape planting"},
    {"id":"planting","group":"Landscaping","name":"Planting","seo":"Garden Planting & Seasonal Care","headline":"Give your garden a fresh start.","summary":"Planting and garden care, including seasonal and recurring cleanups.","body":"New plantings bring color and structure to a yard. Menendez Landscaping provides planting and garden care, with seasonal and recurring cleanups included in the published service description.","points":["Planting for garden and landscape areas","Care for existing garden spaces","Seasonal and recurring cleanups"],"image":"planting.jpeg","alt":"Flowering garden beds at a residential property"},
    {"id":"landscaping-renovation","group":"Landscaping","name":"Landscaping Renovation","seo":"Landscape Renovation & Redesign","headline":"Make an existing yard work better.","summary":"Refresh, modernize or redesign an existing landscape.","body":"A landscape renovation can give an existing outdoor space a clearer layout and a more considered finish. Start with what is already there and what you want to change.","points":["Review existing landscape conditions","Refresh or redesign outdoor areas","Coordinate updates with hardscaping"],"image":"renovation.jpeg","alt":"New stone walkway connected to a residential landscape"},
    {"id":"walkways","group":"Hardscaping","name":"Walkways","seo":"Custom Walkway Installation","headline":"A clear path through your property.","summary":"Custom outdoor walkways designed and installed for your property.","body":"A well-planned walkway connects the home, garden and outdoor living areas. Menendez Landscaping designs and installs custom paths to suit the layout and character of your property.","points":["Custom path layout","Paver and stone walkway options","A clean transition into nearby landscape areas"],"image":"walkways.jpeg","alt":"Stone paver walkway under construction in a residential yard"},
    {"id":"patios","group":"Hardscaping","name":"Patios","seo":"Paver Patio Construction","headline":"A patio made for living outside.","summary":"Patio construction for outdoor dining, relaxing and gathering.","body":"A patio can turn an underused yard into a comfortable place to spend time. Menendez Landscaping builds patios planned around the home, available space and the way you want to use it.","points":["Patio layout around the home and yard","Paver and stone options","A finished outdoor area for everyday use"],"image":"patios.jpeg","alt":"Paved outdoor area with surrounding landscape planting"},
    {"id":"stones-hardscaping","group":"Hardscaping","name":"Stones & Hardscaping","seo":"Stonework & Hardscaping","headline":"Stonework with a purpose.","summary":"Stone features and outdoor structures, including retaining walls.","body":"Stonework can add structure, create useful level changes and define outdoor areas. Menendez Landscaping offers stone and hardscaping work, including retaining walls.","points":["Stone features for outdoor spaces","Retaining walls","Hardscape connections to patios and walkways"],"image":"stonework.jpeg","alt":"Stone steps and landscape wall within a residential yard"},
    {"id":"power-washing","group":"Hardscaping","name":"Power Washing","seo":"Exterior Power Washing","headline":"A cleaner look for outdoor surfaces.","summary":"Pressure washing for driveways, patios, walls and other exterior surfaces.","body":"Outdoor surfaces collect dirt and weathering over time. Power washing can refresh areas such as driveways, patios and exterior walls.","points":["Driveways and paved areas","Patios and outdoor surfaces","Exterior walls and other suitable surfaces"],"image":"power-washing.jpeg","alt":"Paved driveway and stone outdoor surface"},
    {"id":"kitchen-remodeling","group":"Home remodeling","name":"Kitchen Remodeling","seo":"Kitchen Remodeling","headline":"A kitchen that works for home.","summary":"Kitchen renovation and remodeling for residential properties.","body":"A kitchen remodel is a chance to update one of the most-used rooms in the home. Menendez Landscaping provides kitchen remodeling for residential and commercial customers.","points":["Discuss the project scope and existing space","Plan updates around your goals","Coordinate work through a final review"],"image":"kitchen.jpeg","alt":"Kitchen remodeling project in progress"},
    {"id":"floor-remodeling","group":"Home remodeling","name":"Floor Remodeling","seo":"Floor Installation & Remodeling","headline":"New floors. A different feel.","summary":"Floor installation and renovation in laminate, vinyl, tile and wood.","body":"Flooring changes the look and feel of a room. Menendez Landscaping installs and renovates laminate, vinyl, ceramic tile and wood flooring.","points":["Laminate flooring","Vinyl and ceramic tile","Wood floor installation and renovation"],"image":"flooring.jpeg","alt":"Wood flooring inside a residential home"},
    {"id":"bathroom-remodeling","group":"Home remodeling","name":"Bathroom Remodeling","seo":"Bathroom Remodeling","headline":"Refresh the room you use every day.","summary":"Bathroom renovation and remodeling planned around your home.","body":"A bathroom remodel can bring a dated room closer to the way you want your home to work. Menendez Landscaping offers bathroom renovation and remodeling.","points":["Review the existing room and requested updates","Plan a scope suited to the home","Finish with a final project review"],"image":"bathroom.jpeg","alt":"Interior renovation work with tile and trim"},
    {"id":"painting","group":"Home remodeling","name":"Painting","seo":"Interior & Exterior Painting","headline":"A fresh coat inside or out.","summary":"Interior and exterior painting for residential and commercial properties.","body":"A new paint finish can refresh a room or give a home exterior a cleaner look. Menendez Landscaping offers interior and exterior painting.","points":["Interior painting","Exterior painting","Scope based on the surfaces and property"],"image":"painting.jpeg","alt":"Residential home exterior"},
]

GALLERY = [
    ("hero-patio.jpeg","hardscaping","Paver patio & outdoor living","Paver patio and pergola beside a residential home"),
    ("walkways.jpeg","hardscaping","Walkway installation","New paver walkway under construction"),
    ("stonework.jpeg","hardscaping","Stone steps & landscape","Stone steps and retaining wall in a landscaped yard"),
    ("landscaping.jpeg","landscaping","Landscape renovation","Lawn and planting areas with stone edging"),
    ("mulching.jpeg","landscaping","Garden beds","Curved garden beds with flowers and ornamental plants"),
    ("garden.jpeg","landscaping","Planting","Flowering garden beds at a residential property"),
    ("lawn.jpeg","landscaping","Lawn & grounds","Residential lawn and landscape project"),
    ("kitchen.jpeg","remodeling","Kitchen remodeling","Kitchen remodel in progress"),
    ("flooring.jpeg","remodeling","Floor remodeling","Wood flooring inside a home"),
    ("bathroom.jpeg","remodeling","Interior renovation","Interior renovation project with tile and trim"),
    ("patios.jpeg","hardscaping","Patio & planting","Paved outdoor area with landscape planting"),
    ("planting.jpeg","landscaping","Seasonal color","Flower beds with seasonal plantings"),
]

def e(value):
    return escape(str(value), quote=True)

def image(name, alt="", cls="", loading="lazy"):
    return f'<img class="{cls}" src="/images/{name}" alt="{e(alt)}" loading="{loading}" decoding="async">'

def icon(name, cls="icon"):
    svg = (ROOT / "assets" / "icons" / f"{name}.svg").read_text(encoding="utf-8")
    return svg.replace("<svg ", f'<svg class="{e(cls)}" aria-hidden="true" focusable="false" ', 1)

def route_url(route=""):
    return f"/{route}/" if route else "/"

def header(active=""):
    links = [("home","/","Home"),("about","/about/","About"),("gallery","/gallery/","Gallery"),("contact","/contact/","Contact")]
    nav_links = []
    for key,url,label in links:
        current = ' aria-current="page"' if active == key else ""
        class_name = ' class="home-nav-link"' if key == "home" else ""
        nav_links.append(f'<a{class_name} href="{url}"{current}>{label}</a>')
    service_links = "".join(f'<a href="/services/{item["id"]}/">{e(item["name"])}</a>' for item in SERVICES)
    service_active = " is-active" if active == "services" else ""
    service_dropdown = f'''<div class="nav-dropdown" data-service-dropdown>
        <button class="nav-dropdown__trigger{service_active}" type="button" aria-expanded="false" aria-controls="service-nav-panel">Services<span class="nav-dropdown__chevron" aria-hidden="true"></span></button>
        <div class="nav-dropdown__panel" id="service-nav-panel" hidden>
          <a class="nav-dropdown__all" href="/services/">All services <span>Browse all 13 services</span></a>
          {service_links}
        </div>
      </div>'''
    nav = "".join([nav_links[0], service_dropdown] + nav_links[1:])
    return f'''<header class="site-header"><div class="site-header__inner">
      <a class="brand" href="/" aria-label="Menendez Landscaping home">{image("brand-mark.png","Menendez Landscaping","brand__image","eager")}</a>
      <a class="home-shortcut" href="/"{" aria-current=\"page\"" if active == "home" else ""}>Home</a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="primary-nav"><span class="menu-toggle__lines" aria-hidden="true"></span><span class="sr-only">Open menu</span></button>
      <nav class="primary-nav" id="primary-nav" aria-label="Main navigation">{nav}
        <a class="header-phone" href="tel:{PHONE_HREF}">{icon("phone")}<span>{PHONE}</span></a><a class="button button--accent button--small" href="/contact/">Free estimate {icon("arrow-right")}</a>
      </nav>
    </div></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="footer-main shell">
      <div class="footer-brand"><a class="brand brand--footer" href="/" aria-label="Menendez Landscaping home">{image("brand-mark.png","Menendez Landscaping","brand__image")}</a><p>Landscaping, hardscaping &amp; home remodeling in Hamilton, NJ.</p></div>
      <div class="footer-links"><h2>Services</h2><a href="/services/">All services</a><a href="/services/landscaping/">Landscaping</a><a href="/services/patios/">Patios</a><a href="/services/kitchen-remodeling/">Home remodeling</a></div>
      <div class="footer-links"><h2>Company</h2><a href="/about/">About us</a><a href="/gallery/">Our work</a><a href="/contact/">Contact</a></div>
      <div class="footer-links footer-links--contact"><h2>Get in touch</h2><a href="tel:{PHONE_HREF}">{icon("phone")}<span>{PHONE}</span></a><a href="mailto:{EMAIL}">{icon("mail")}<span>{EMAIL}</span></a><span>{icon("map-pin")}<span>Hamilton, NJ</span></span></div>
      <div class="footer-links footer-links--social"><h2>Follow us</h2>{''.join(f'<a href="{e(url)}" target="_blank" rel="noopener noreferrer">{e(label)}</a>' for label, url in SOCIAL_LINKS)}</div>
    </div><div class="footer-bottom shell"><span>© {date.today().year} Menendez Landscaping LLC</span><span>Residential &amp; commercial · Free estimates</span></div></footer>'''

def schema_tag(data):
    serialized = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    return f'<script type="application/ld+json">{serialized}</script>'

def layout(title, description, content, route="", active="", preload="", body_class="", extra_schema=None):
    canonical = SITE + route_url(route)
    schema = {"@context":"https://schema.org","@type":["HomeAndConstructionBusiness","LocalBusiness"],"@id":SITE + "/#business","name":"Menendez Landscaping LLC","url":SITE,"telephone":PHONE_HREF,"email":EMAIL,"logo":SITE + "/images/brand-mark.png","image":SITE + "/images/" + (preload or "hero-patio.jpeg"),"sameAs":[url for _, url in SOCIAL_LINKS],"address":{"@type":"PostalAddress","addressLocality":"Hamilton","addressRegion":"NJ","postalCode":"08611","addressCountry":"US"},"areaServed":{"@type":"City","name":"Hamilton, New Jersey"},"serviceType":[item["name"] for item in SERVICES],"contactPoint":{"@type":"ContactPoint","telephone":PHONE_HREF,"email":EMAIL,"contactType":"customer service","areaServed":"US"}}
    preload_tag = f'<link rel="preload" as="image" href="/images/{preload}" fetchpriority="high">' if preload else ""
    extra_schema_tag = "".join(schema_tag(item) for item in (extra_schema if isinstance(extra_schema, list) else [extra_schema]) if item)
    social_image = SITE + "/images/" + (preload or "hero-patio.jpeg")
    return f'''<!doctype html><html lang="en"><head>
      <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#fffdf8"><meta name="robots" content="index,follow,max-image-preview:large">
      <title>{e(title)}</title><meta name="description" content="{e(description)}"><link rel="canonical" href="{canonical}"><link rel="manifest" href="/site.webmanifest"><link rel="icon" href="/assets/icons/tree.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/images/brand-mark.png">
      <meta property="og:type" content="website"><meta property="og:site_name" content="Menendez Landscaping LLC"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{social_image}"><meta property="og:image:alt" content="Landscaping and hardscaping project by Menendez Landscaping in Hamilton, NJ">
      <meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(description)}"><meta name="twitter:image" content="{social_image}">
      {preload_tag}<link rel="stylesheet" href="/assets/css/site.css">{schema_tag(schema)}{extra_schema_tag}<script src="/assets/js/site.js" defer></script>
      </head><body class="{body_class}"><a class="skip-link" href="#main">Skip to content</a>{header(active)}<main id="main">{content}</main>{footer()}
      <a class="whatsapp-float" href="{WHATSAPP}" target="_blank" rel="noopener noreferrer" aria-label="Message Menendez Landscaping on WhatsApp"><span class="whatsapp-float__mark">{icon("brand-whatsapp")}</span><span class="whatsapp-float__label">WhatsApp</span></a>
      </body></html>'''

def cta_button(service_id=""):
    destination = f"/contact/?service={service_id}" if service_id else "/contact/"
    return f'<a class="button button--accent" href="{destination}">Get a free estimate {icon("arrow-right")}</a>'

def home_page():
    home_groups = []
    for group in GROUPS:
        items = [item for item in SERVICES if item["group"] == group["name"]]
        links = "".join(f'<li><a href="/services/{item["id"]}/">{e(item["name"])}{icon("arrow-up-right")}</a></li>' for item in items)
        group_icon = {"Landscaping":"leaf","Hardscaping":"tools","Home remodeling":"home"}[group["name"]]
        home_groups.append(f'''<article class="home-service" data-reveal>
          <a class="home-service__photo" href="/services/#{group["id"]}" aria-label="Explore {e(group["name"])} services">{image(group["image"],group["alt"])}</a>
          <div class="home-service__heading"><span class="home-service__icon">{icon(group_icon)}</span><h3>{e(group["name"])}</h3></div>
          <p>{e(group["intro"])}</p><ul class="home-service__links">{links}</ul>
        </article>''')

    home_gallery = [
        ("hero-patio.jpeg","Patio & hardscaping","Paver patio and outdoor living area"),
        ("landscaping.jpeg","Landscape renovation","Garden beds and stone landscape edging"),
        ("mulching.jpeg","Mulching & planting","Fresh mulch and established planting beds"),
        ("kitchen.jpeg","Kitchen remodeling","Residential kitchen remodeling project"),
    ]
    gallery_cards = "".join(
        f'<a class="work-item work-item--{("feature" if i == 0 else "wide" if i == 1 else "small")}" href="/gallery/">{image(photo,alt)}<span class="work-item__caption">{label}{icon("arrow-up-right")}</span></a>'
        for i,(photo,label,alt) in enumerate(home_gallery)
    )
    process_steps = [
        ("message","Tell us about the project","Share the service, property and location."),
        ("clipboard-check","Review the scope","Discuss the work and estimate."),
        ("check","Complete & review","Finish the agreed work and walk through details."),
    ]
    process_html = "".join(
        f'<li data-reveal><span class="process-step__icon">{icon(icon_name)}</span><span class="process-step__number">0{i+1}</span><h3>{title}</h3><p>{copy}</p></li>'
        for i,(icon_name,title,copy) in enumerate(process_steps)
    )
    faqs = [
        ("What services does Menendez Landscaping offer?","The company offers landscaping and garden care, patios, walkways, stonework, power washing, and home remodeling."),
        ("Where does Menendez Landscaping work?","The company is based in Hamilton, New Jersey, and advertises an approximate 50–70 mile service radius. Share your town or ZIP to confirm coverage."),
        ("How do I request a free estimate?","Call (609) 516-6584, email info@menendezlandscapingnj.com, or send your project details through the contact form."),
    ]
    faq_html = "".join(
        f'<details class="faq-item"{" open" if i == 0 else ""}><summary>{question}{icon("plus")}</summary><p>{answer}</p></details>'
        for i,(question,answer) in enumerate(faqs)
    )
    faq_schema = {
        "@context":"https://schema.org",
        "@type":"FAQPage",
        "mainEntity":[
            {"@type":"Question","name":question,"acceptedAnswer":{"@type":"Answer","text":answer}}
            for question,answer in faqs
        ],
    }
    content = f'''<section class="hero hero--home" aria-labelledby="home-title">
      {image("patios.jpeg","Paver patio with outdoor seating and stone landscaping","hero__image","eager")}<div class="hero__shade"></div>
      <div class="hero__content shell">
        <p class="eyebrow eyebrow--light hero__location">{icon("map-pin")} Hamilton, New Jersey</p>
        <h1 id="home-title">Landscaping, hardscaping <span>&amp; home remodeling.</span></h1>
        <p class="hero__lede">Residential &amp; commercial projects. Free estimates.</p>
        <div class="hero__actions">{cta_button()}<a class="button button--outline-light" href="tel:{PHONE_HREF}">{icon("phone")} Call {PHONE}</a></div>
        <div class="hero__services" aria-label="Main services"><a href="/services/landscaping/">Landscaping</a><a href="/services/patios/">Patios &amp; stonework</a><a href="/services/kitchen-remodeling/">Home remodeling</a></div>
      </div>
    </section>
    <section class="home-about section shell" aria-labelledby="about-title">
      <div class="home-about__copy" data-reveal><p class="eyebrow">About Menendez Landscaping</p><h2 id="about-title">Family-owned. Built on experience.</h2>
        <p>Menendez Landscaping LLC is a family-owned business based in Hamilton, NJ, with more than 15 years of experience. The team works on residential and commercial landscapes, outdoor construction and home remodeling.</p>
        <a class="text-link" href="/about/">More about us {icon("arrow-right")}</a>
      </div>
      <figure class="home-about__figure" data-reveal>{image("landscaping.jpeg","Landscape beds, lawn and stone edging at a residential property")}
        <figcaption><strong>15+</strong><span>years of experience</span></figcaption>
      </figure>
    </section>
    <section class="home-services section" aria-labelledby="home-services-title">
      <div class="shell"><div class="section-heading section-heading--center"><p class="eyebrow">Services</p><h2 id="home-services-title">One team for outside and in.</h2><p>Landscaping, patios and stonework, plus home remodeling.</p></div>
        <div class="home-service-grid">{''.join(home_groups)}</div>
        <div class="section-tail"><a class="text-link" href="/services/">See all 13 services {icon("arrow-right")}</a></div>
      </div>
    </section>
    <section class="section work-preview shell" aria-labelledby="work-title">
      <div class="section-heading section-heading--work"><div><p class="eyebrow">Our work</p><h2 id="work-title">See the difference in the details.</h2></div><a class="text-link" href="/gallery/">View all projects {icon("arrow-right")}</a></div>
      <div class="work-grid">{gallery_cards}</div>
    </section>
    <section class="process-section" aria-labelledby="process-title"><div class="shell">
      <div class="section-heading"><p class="eyebrow eyebrow--light">A straightforward process</p><h2 id="process-title">From first call to finished work.</h2></div>
      <ol class="process-list">{process_html}</ol>
    </div></section>
    <section class="area-section section shell" aria-labelledby="area-title">
      <figure class="area-section__photo">{image("walkways.jpeg","Stone walkway and landscaping at a residential property")}</figure>
      <div class="area-section__copy" data-reveal><p class="eyebrow">{icon("map-pin")} Service area</p><h2 id="area-title">Based in Hamilton, NJ.</h2>
        <p>Residential and commercial projects within an approximate 50–70 mile radius. Share your town or ZIP and the team can confirm coverage.</p>
        <div class="area-tags"><span>{icon("home")} Residential</span><span>{icon("building")} Commercial</span></div>
        <a class="button button--outline-dark" href="/contact/">Ask about your location {icon("arrow-right")}</a>
      </div>
    </section>
    <section class="faq-section section shell" aria-labelledby="faq-title">
      <div class="section-heading"><p class="eyebrow">Common questions</p><h2 id="faq-title">A few things to know before you start.</h2></div>
      <div class="faq-list">{faq_html}</div>
    </section>
    <section class="closing-hero closing-hero--home" aria-labelledby="closing-title">
      {image("patios.jpeg","","closing-hero__image")}<div class="closing-hero__shade"></div>
      <div class="closing-hero__content shell"><p class="eyebrow eyebrow--light">Let’s talk about your project</p><h2 id="closing-title">Ready for a fresh start outside or in?</h2>
        <p>Tell us what you want to build. Free estimates in Hamilton and nearby communities.</p>
        <div class="hero__actions">{cta_button()}<a class="button button--outline-light" href="tel:{PHONE_HREF}">{icon("phone")} {PHONE}</a></div>
      </div>
      <aside class="closing-hero__contact"><a href="tel:{PHONE_HREF}">{icon("phone")}<span><small>Call</small>{PHONE}</span></a><a href="mailto:{EMAIL}">{icon("mail")}<span><small>Email</small>{EMAIL}</span></a></aside>
    </section>'''
    return layout(
        "Landscaping, Hardscaping & Remodeling in Hamilton, NJ | Menendez Landscaping",
        "Family-owned Menendez Landscaping provides landscaping, patios, walkways, stonework and home remodeling in Hamilton, NJ. Call for a free estimate.",
        content,active="home",preload="patios.jpeg",body_class="page-home",extra_schema=faq_schema
    )

def services_page():
    blocks = []
    headlines = {"Landscaping":"Bring the landscape together.","Hardscaping":"Build more useful outdoor space.","Home remodeling":"Make the inside feel right."}
    for group in GROUPS:
        items = [x for x in SERVICES if x["group"] == group["name"]]
        rows = "".join(f'<a class="service-row" href="/services/{item["id"]}/"><span><strong>{item["name"]}</strong><small>{item["summary"]}</small></span><span aria-hidden="true">↗</span></a>' for item in items)
        blocks.append(f'''<section class="service-group" id="{group["id"]}"><div class="service-group__image-wrap">{image(group["image"],group["alt"],"service-group__image")}<span class="service-group__image-label">{group["name"]}</span></div><div class="service-group__content"><p class="eyebrow">{group["name"]}</p><h2>{headlines[group["name"]]}</h2><p>{group["intro"]}</p><div class="service-list">{rows}</div></div></section>''')
    content = f'''<section class="page-intro shell"><div><p class="eyebrow">Our services · Hamilton, NJ</p><h1>Outdoor projects and home updates, handled by one team.</h1></div><p>Explore 13 services across landscaping, hardscaping and home remodeling. Each service has its own page with details and a direct estimate link.</p></section><div class="service-groups shell">{"".join(blocks)}</div><section class="cta-strip shell"><div><p class="eyebrow eyebrow--light">Start with your project</p><h2>Not sure which service fits?</h2><p>Describe the work and the team can help discuss the next step.</p></div><div class="cta-strip__actions">{cta_button()}<a class="button button--outline-light" href="tel:{PHONE_HREF}">Call {PHONE}</a></div></section>'''
    return layout("Landscaping & Remodeling Services | Menendez Landscaping","Browse all 13 Menendez Landscaping services in Hamilton, NJ: landscaping, mulching, pruning, patios, walkways, stonework and home remodeling.",content,"services","services",body_class="page-services")

def service_page(item):
    related = [x for x in SERVICES if x["group"] == item["group"] and x["id"] != item["id"]][:3]
    points = "".join(f'<li>{point}</li>' for point in item["points"])
    links = "".join(f'<a class="related-link" href="/services/{x["id"]}/"><span>{x["name"]}</span><span aria-hidden="true">↗</span></a>' for x in related)
    steps = [("01","Assess & plan","Review the property, goals and project scope."),("02","Prepare & set up","Plan the work area, materials and next steps."),("03","Complete the work","Carry out the agreed service for your property."),("04","Review the finish","Go through the final details together.")]
    step_html = "".join(f'<li><span class="process-list__number">{n}</span><h3>{t}</h3><p>{d}</p></li>' for n,t,d in steps)
    content = f'''<section class="service-hero shell"><div class="service-hero__copy"><p class="eyebrow">{item["group"]} / Hamilton, NJ</p><h1>{item["headline"]}</h1><p class="service-hero__lede">{item["body"]}</p><div class="hero__actions">{cta_button(item["id"])}<a class="text-link" href="tel:{PHONE_HREF}">Call {PHONE} <span aria-hidden="true">→</span></a></div><a class="breadcrumb" href="/services/">← All services</a></div><figure class="service-hero__figure">{image(item["image"],item["alt"],"service-hero__image","eager")}<figcaption>{item["name"]} · Menendez Landscaping</figcaption></figure></section>
    <section class="section service-detail shell"><div><p class="eyebrow">About this service</p><h2>{item["name"]}, planned for your property.</h2><p>{item["summary"]} The exact scope depends on the property and work requested.</p></div><div class="service-detail__points"><h3>Project considerations</h3><ul class="check-list">{points}</ul><p class="small-note">Ask for a free estimate to discuss your project details.</p></div></section>
    <section class="service-process"><div class="shell"><div class="section-heading section-heading--split"><div><p class="eyebrow eyebrow--light">Project process</p><h2>A clear path from first look to final review.</h2></div><p>The steps vary by service, but each project starts with a conversation about the property and the work you need.</p></div><ol class="process-list">{step_html}</ol></div></section>
    <section class="section related-section shell"><div class="section-heading section-heading--split"><div><p class="eyebrow">Related services</p><h2>Keep the project moving.</h2></div><p>Explore related work or tell us what you have in mind.</p></div><div class="related-list">{links}</div></section>
    <section class="closing-hero closing-hero--short">{image(item["image"],"","closing-hero__image")}<div class="closing-hero__shade"></div><div class="closing-hero__content shell"><p class="eyebrow eyebrow--light">{item["name"]} · Hamilton, NJ</p><h2>Let’s discuss your project.</h2><p>Call or send a project request to get started.</p><div class="hero__actions">{cta_button(item["id"])}<a class="button button--outline-light" href="tel:{PHONE_HREF}">Call {PHONE}</a></div></div></section>'''
    title = f'{item["seo"]} in Hamilton, NJ | Menendez Landscaping'
    description = f'{item["summary"]} Menendez Landscaping is family-owned and based in Hamilton, NJ. Request a free estimate.'
    service_schema = {"@context":"https://schema.org","@type":"Service","@id":SITE + route_url(f'services/{item["id"]}') + "#service","name":item["name"],"description":item["summary"],"serviceType":item["name"],"provider":{"@id":SITE + "/#business"},"areaServed":{"@type":"City","name":"Hamilton, New Jersey"}}
    return layout(title,description,content,f'services/{item["id"]}',"services",item["image"],"page-service",extra_schema=service_schema)

def about_page():
    content = f'''<section class="about-hero shell"><div class="about-hero__copy"><p class="eyebrow">About Menendez Landscaping</p><h1>A family-owned team for the spaces around your home.</h1><p>Based in Hamilton, New Jersey, Menendez Landscaping LLC serves residential and commercial customers with landscaping, hardscaping and home remodeling. The company reports more than 15 years of experience.</p><div class="hero__actions">{cta_button()}<a class="text-link" href="tel:{PHONE_HREF}">Call {PHONE} <span aria-hidden="true">→</span></a></div></div><figure class="about-hero__figure">{image("hero-patio.jpeg","Paver patio and pergola at a residential property","about-hero__image","eager")}<figcaption>Outdoor work by Menendez Landscaping</figcaption></figure></section>
    <section class="proof-band"><div class="proof-band__inner shell"><p><strong>Family owned</strong><span>personal attention</span></p><p><strong>15+ years</strong><span>of experience</span></p><p><strong>Hamilton, NJ</strong><span>local point of reference</span></p><p><strong>Free estimates</strong><span>project conversations start here</span></p></div></section>
    <section class="section about-values shell"><div class="section-heading section-heading--split"><div><p class="eyebrow">How we approach the work</p><h2>Good work starts with listening.</h2></div><p>The company emphasizes quality, integrity, reliability and customer-focused service. Those values shape how a project is discussed and carried through.</p></div><div class="values-grid"><article><span>01</span><h3>Quality</h3><p>Careful work and attention to the finished details.</p></article><article><span>02</span><h3>Integrity</h3><p>Clear communication and responsible project planning.</p></article><article><span>03</span><h3>Customer focus</h3><p>A conversation shaped around the property and your goals.</p></article></div></section>
    <section class="process-section"><div class="shell"><div class="section-heading section-heading--split"><div><p class="eyebrow eyebrow--light">Our process</p><h2>A practical plan for each project.</h2></div><p>The steps are adjusted to the service and property, with planning and a final review built in.</p></div><ol class="process-list"><li><span class="process-list__number">01</span><h3>Assessment &amp; planning</h3><p>Discuss the property, the work and the project goals.</p></li><li><span class="process-list__number">02</span><h3>Preparation &amp; setup</h3><p>Prepare the site, materials and work area.</p></li><li><span class="process-list__number">03</span><h3>Maintenance &amp; care</h3><p>Carry out the planned work and care for the project area.</p></li><li><span class="process-list__number">04</span><h3>Final touch &amp; review</h3><p>Review the finish and address the last details.</p></li></ol></div></section>
    <section class="section about-contact shell"><div>{image("garden.jpeg","Flowering garden at a residential property","about-contact__photo")}</div><div><p class="eyebrow">Start a conversation</p><h2>Tell us what you want to improve.</h2><p>Share your service, town and a few details about the property. Free project estimates are available.</p>{cta_button()}</div></section>'''
    return layout("About Menendez Landscaping | Hamilton, NJ","Meet Menendez Landscaping LLC, a family-owned Hamilton, NJ company offering landscaping, hardscaping and home remodeling with 15+ years of experience.",content,"about","about",body_class="page-about")

def gallery_page():
    filters = [("all","All work"),("landscaping","Landscaping"),("hardscaping","Hardscaping"),("remodeling","Remodeling")]
    buttons = "".join(f'<button type="button" class="filter-button{" is-active" if i==0 else ""}" data-filter="{v}" aria-pressed="{str(i==0).lower()}">{label}</button>' for i,(v,label) in enumerate(filters))
    cards = "".join(f'<a class="gallery-card{" gallery-card--tall" if i%5==0 else ""}" href="/contact/" data-category="{category}"><span class="gallery-card__image">{image(photo,alt)}</span><span class="gallery-card__caption"><span>{label}</span><small>{category.title()}</small></span></a>' for i,(photo,category,label,alt) in enumerate(GALLERY))
    content = f'''<section class="page-intro shell"><div><p class="eyebrow">Project gallery</p><h1>Work across yards, paths and interiors.</h1></div><p>Browse selected project photos from Menendez Landscaping. Ask the team about work that fits your property.</p></section><section class="gallery-section shell" aria-label="Project photos"><div class="gallery-filters" role="group" aria-label="Filter project photos">{buttons}</div><div class="gallery-grid">{cards}</div></section><section class="cta-strip shell"><div><p class="eyebrow eyebrow--light">A project of your own</p><h2>Want to see what’s possible at your property?</h2><p>Send a few details and request a free estimate.</p></div><div class="cta-strip__actions">{cta_button()}<a class="button button--outline-light" href="tel:{PHONE_HREF}">Call {PHONE}</a></div></section>'''
    return layout("Project Gallery | Menendez Landscaping","View landscaping, hardscaping and home remodeling photos from Menendez Landscaping in Hamilton, New Jersey.",content,"gallery","gallery",body_class="page-gallery")

def contact_page():
    options = "".join(f'<option value="{item["id"]}">{item["name"]}</option>' for item in SERVICES)
    content = f'''<section class="page-intro shell"><div><p class="eyebrow">Contact · Hamilton, NJ</p><h1>Tell us about your project.</h1></div><p>Share the service, your town and what you would like to improve. Free estimates are available for landscaping and remodeling projects.</p></section>
    <section class="contact-layout shell"><div class="contact-photo">{image("walkways.jpeg","Paver walkway in a residential landscape","contact-photo__image")}<div class="contact-photo__note"><span>Menendez Landscaping</span><strong>Outdoor spaces, built with care.</strong></div></div><div class="contact-form-wrap"><h2>Request a free estimate</h2><p>Add the details you know. You can discuss the project scope with the team.</p><form class="contact-form" action="https://formsubmit.co/{EMAIL}" method="POST" data-ajax-endpoint="https://formsubmit.co/ajax/{EMAIL}" data-contact-form>
      <input type="hidden" name="_subject" value="New estimate request from Menendez Landscaping website"><input type="hidden" name="_url" value="{SITE}/contact/">
      <div class="form-honeypot" aria-hidden="true"><label>Leave this field empty<input name="_honey" tabindex="-1" autocomplete="off"></label></div>
      <div class="field-row"><label>First name<input name="first_name" autocomplete="given-name" required></label><label>Last name<input name="last_name" autocomplete="family-name" required></label></div>
      <div class="field-row"><label>Phone number<input type="tel" name="phone" autocomplete="tel" required></label><label>Email address<input type="email" name="email" autocomplete="email" required></label></div>
      <div class="field-row"><label>Service<select name="service" id="service-select" required><option value="">Select a service</option>{options}</select></label><label>Town or ZIP code<input name="town_or_zip" autocomplete="postal-code" required></label></div>
      <label>Project details<textarea name="project_details" rows="5" placeholder="What would you like to work on?" required></textarea></label><button class="button button--accent" type="submit"><span class="submit-label">Send estimate request</span>{icon("arrow-right")}</button>
      <p class="form-note" id="form-status" role="status" aria-live="polite">Share your details and the team will follow up. For a quicker response, call (609) 516-6584.</p></form>
      <div class="contact-details"><div><span class="eyebrow">Call</span><a href="tel:{PHONE_HREF}">{PHONE}</a></div><div><span class="eyebrow">Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></div><div><span class="eyebrow">Based in</span><span>Hamilton, NJ</span></div></div></div></section>
    <section class="contact-note shell"><p><strong>Checking service area?</strong> The company advertises an approximate 50–70 mile radius from Hamilton. Share your town or ZIP so the team can confirm availability.</p><a class="text-link" href="{WHATSAPP}" target="_blank" rel="noopener noreferrer">Message on WhatsApp <span aria-hidden="true">→</span></a></section>'''
    return layout("Contact Menendez Landscaping | Free Estimates in Hamilton, NJ",f"Contact Menendez Landscaping in Hamilton, NJ. Call {PHONE} or request a free estimate for landscaping, hardscaping or remodeling.",content,"contact","contact",body_class="page-contact")

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "images").mkdir(parents=True, exist_ok=True)
(OUT / "assets" / "css").mkdir(parents=True, exist_ok=True)
(OUT / "assets" / "js").mkdir(parents=True, exist_ok=True)
(OUT / "assets" / "icons").mkdir(parents=True, exist_ok=True)
shutil.copy2(ROOT / "assets" / "css" / "site.css", OUT / "assets" / "css" / "site.css")
shutil.copytree(ROOT / "assets" / "icons", OUT / "assets" / "icons", dirs_exist_ok=True)
for stale_asset in (OUT / "assets" / "video" / "home-garden.mp4", OUT / "images" / "hero-video-poster.webp"):
    stale_asset.unlink(missing_ok=True)
for destination, source in MEDIA.items():
    original = ROOT / "LOGO" / "47d7c6b5-6dac-41ad-bddf-2c20d2237608-Photoroom.png" if destination == "brand-mark.png" else ROOT / "FOTOS" / source
    shutil.copy2(original, OUT / "images" / destination)
shutil.copy2(ROOT / "assets" / "icons" / "tree.svg", OUT / "favicon.svg")
(OUT / "site.webmanifest").write_text(json.dumps({"name":"Menendez Landscaping LLC","short_name":"Menendez","start_url":"/","display":"standalone","background_color":"#fffdf8","theme_color":"#173d30","icons":[{"src":"/images/brand-mark.png","sizes":"any","type":"image/png"}]}, ensure_ascii=False, indent=2), encoding="utf-8")

def write_page(route, html):
    folder = OUT / route if route else OUT
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "index.html").write_text(html, encoding="utf-8")

write_page("", home_page())
write_page("services", services_page())
write_page("about", about_page())
write_page("gallery", gallery_page())
write_page("contact", contact_page())
for item in SERVICES:
    write_page(f'services/{item["id"]}', service_page(item))

routes = ["", "services", "about", "gallery", "contact"] + [f'services/{item["id"]}' for item in SERVICES]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f'  <url><loc>{SITE}{route_url(route)}</loc></url>\n' for route in routes) + '</urlset>\n'
(OUT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
(ROOT / "README.md").write_text("""# Menendez Landscaping website

Install frontend dependencies once: `npm install`
Build static pages and the locally bundled Anime.js animations: `npm run build`
Preview the generated files: `python -m http.server 4173 --directory public`
Then open http://localhost:4173

The estimate form posts to FormSubmit. Its first submission is held until the one-time activation link sent to info@menendezlandscapingnj.com is opened.
The WhatsApp button uses the published business phone number; confirm the number is registered with WhatsApp before launch.
Social profile links were supplied by the business and are included in the footer and LocalBusiness schema.
The home hero uses a project photo from the provided FOTOS collection.
""", encoding="utf-8")
print(f"Generated {len(routes)} pages and {len(MEDIA)} image assets in public/.")
