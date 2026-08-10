from pathlib import Path

ROOT = Path(r"C:\Users\ThanhThien\.cursor\dsquare website")

NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("work.html", "Work"),
    ("insights.html", "Insights"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]


def page(title, purpose, active, body):
    nav_items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        nav_items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    nav = "\n            ".join(nav_items)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{purpose}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Syne:wght@600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/css/main.css" />
</head>
<body>
  <a class="sr-only" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="container nav">
      <a class="logo" href="index.html" aria-label="DSQUARE home">
        <span class="logo-mark" aria-hidden="true">D2</span>
        DSQUARE
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
        <span></span><span></span><span></span>
      </button>
      <ul class="nav-links" id="site-nav">
            {nav}
        <li class="nav-cta"><a class="btn btn-primary" href="contact.html">Talk to us</a></li>
      </ul>
    </div>
  </header>
  <main id="main">
{body}
  </main>
  <footer class="site-footer">
    <div class="container">
      <div class="footer-brand">DSQUARE</div>
      <div class="footer-grid">
        <div>
          <p class="text-white" style="margin:0 0 .7rem;font-weight:700;">Growth Partner Agency in Vietnam</p>
          <p style="margin:0;max-width:28rem;">Brand &amp; Communication · Customer Experience &amp; CRM · Commerce · Digital Solutions &amp; Innovation</p>
        </div>
        <div>
          <h4>Work</h4>
          <ul>
            <li><a href="work.html">All work</a></li>
            <li><a href="work-suzuki-fronx.html">Suzuki Fronx</a></li>
            <li><a href="work-ariston.html">Ariston Ice Challenge</a></li>
            <li><a href="work-mitsubishi.html">Mitsubishi CDI</a></li>
            <li><a href="work-gojek.html">Gojek Achieve More</a></li>
          </ul>
        </div>
        <div>
          <h4>Services</h4>
          <ul>
            <li><a href="services.html#brand-communication">Brand &amp; Communication</a></li>
            <li><a href="services.html#cx-crm">CX &amp; CRM</a></li>
            <li><a href="services.html#commerce">Commerce</a></li>
            <li><a href="services.html#digital-solutions">Digital Solutions</a></li>
          </ul>
        </div>
        <div>
          <h4>Insights</h4>
          <ul>
            <li><a href="insights.html">All insights</a></li>
            <li><a href="insight-fragmented-operating-models.html">Fragmented digital models</a></li>
            <li><a href="insight-marketing-sales-loop.html">Marketing-to-sales loop</a></li>
            <li><a href="insight-brand-quality-proof.html">When quality stops being felt</a></li>
          </ul>
        </div>
        <div>
          <h4>Company</h4>
          <ul>
            <li><a href="about.html">About</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="aeo-review.html">AEO Review</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© DSQUARE · Square Direct Advertising Company Limited</span>
        <span><a href="mailto:thework@dsquare.com.vn">thework@dsquare.com.vn</a></span>
      </div>
    </div>
  </footer>
  <a class="btn btn-ghost review-toggle" href="aeo-review.html">AEO Review</a>
  <script src="assets/js/main.js"></script>
</body>
</html>
"""


def pillar(anchor, num, title, proposition, problems, capabilities, work_links, insight_links):
    work = "\n".join(f'<a href="{h}">{t}</a>' for h, t in work_links)
    insights = "\n".join(f'<a href="{h}">{t}</a>' for h, t in insight_links)
    problems_li = "\n".join(f"<li>{p}</li>" for p in problems)
    caps_li = "\n".join(f"<li>{c}</li>" for c in capabilities)
    return f"""
    <article class="pillar" id="{anchor}">
      <div class="pillar-grid reveal">
        <div>
          <p class="eyebrow">{num}</p>
          <h2>{title}</h2>
          <p class="lead">{proposition}</p>
          <div class="btn-row">
            <a class="btn btn-primary" href="contact.html">Talk about this</a>
          </div>
        </div>
        <div class="detail-list">
          <div class="detail-box">
            <h4>Problems we solve</h4>
            <ul>{problems_li}</ul>
          </div>
          <div class="detail-box">
            <h4>Capabilities</h4>
            <ul>{caps_li}</ul>
          </div>
          <div class="detail-box">
            <h4>Relevant work</h4>
            <div class="related-links">{work}</div>
          </div>
          <div class="detail-box">
            <h4>Related insights</h4>
            <div class="related-links">{insights}</div>
          </div>
        </div>
      </div>
    </article>
"""


files = {}

files["index.html"] = page(
    "DSQUARE — Growth Partner Agency in Vietnam",
    "DSQUARE is a Growth Partner Agency in Vietnam helping brands grow through Brand & Communication, Customer Experience & CRM, Commerce, and Digital Solutions & Innovation.",
    "index.html",
    """
    <section class="hero">
      <div class="hero-media" aria-hidden="true">
        <img src="assets/images/work-suzuki-fronx.jpg" alt="" />
      </div>
      <div class="container hero-content reveal">
        <p class="brand-signal">DSQUARE</p>
        <p class="campaign-kicker">Featured work · Suzuki All-new Fronx</p>
        <h1>Launching a new edge for Suzuki Fronx.</h1>
        <div class="hero-panel">
          <p class="positioning">
            DSQUARE is a <strong>Growth Partner Agency in Vietnam</strong>.
            We help brands grow through Brand &amp; Communication, Customer Experience &amp; CRM, Commerce, and Digital Solutions &amp; Innovation.
          </p>
        </div>
        <div class="btn-row">
          <a class="btn btn-primary" href="work.html">Our work</a>
          <a class="btn btn-ghost" href="services.html">What we do</a>
        </div>
      </div>
    </section>

    <div class="rule" aria-hidden="true"></div>

    <section class="section">
      <div class="container">
        <div class="split reveal">
          <div>
            <p class="eyebrow">Who we are</p>
            <p class="voice-line">We fuse sharp ideas with the right tech, and simply get the job done.</p>
            <p class="lead">Zero buzzwords. Just trust from day one. DSQUARE sits with brands as a growth partner — connecting campaigns, customer systems, commerce, and digital builds so the work compounds.</p>
            <div class="btn-row">
              <a class="btn btn-ghost" href="about.html">About DSQUARE</a>
            </div>
          </div>
          <div class="media-frame float-slow">
            <img src="assets/images/brand-hands-square.png" alt="DSQUARE brand visual — collaboration forming a square" />
          </div>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:0;">
      <div class="container">
        <div class="section-head row reveal">
          <div>
            <p class="eyebrow">What we do</p>
            <h2>Four capabilities. One partner.</h2>
            <p class="lead">The same names you’ll see on Services, Work, and Insights — so it’s always clear what DSQUARE owns.</p>
          </div>
          <a class="btn btn-ghost" href="services.html">All services</a>
        </div>
        <div class="capability-grid">
          <a class="capability-card reveal" href="services.html#brand-communication">
            <span class="num">01</span>
            <div>
              <h3>Brand &amp; Communication</h3>
              <p>We don’t like seeing another ad either. We strip corporate speak and craft stories people actually want to see.</p>
              <span class="link-label">View →</span>
            </div>
          </a>
          <a class="capability-card reveal" href="services.html#cx-crm">
            <span class="num">02</span>
            <div>
              <h3>Customer Experience &amp; CRM</h3>
              <p>Keep the relationship useful after the click — journeys, loyalty, and customer data that sales and care can act on.</p>
              <span class="link-label">View →</span>
            </div>
          </a>
          <a class="capability-card reveal" href="services.html#commerce">
            <span class="num">03</span>
            <div>
              <h3>Commerce</h3>
              <p>Yep, we hate the hassle as much as you do. Turn data into clear answers and storefronts that just work.</p>
              <span class="link-label">View →</span>
            </div>
          </a>
          <a class="capability-card reveal" href="services.html#digital-solutions">
            <span class="num">04</span>
            <div>
              <h3>Digital Solutions &amp; Innovation</h3>
              <p>Build the platforms and integrations that let strategy run — not another deck that stops at recommendations.</p>
              <span class="link-label">View →</span>
            </div>
          </a>
        </div>
      </div>
    </section>

    <section class="section" style="background:#08080a;">
      <div class="container">
        <div class="section-head row reveal">
          <div>
            <p class="eyebrow">Our work</p>
            <h2>Campaigns that actually made an impact.</h2>
            <p class="lead">We prefer to let the work run the show — tagged to the capabilities behind it.</p>
          </div>
          <a class="btn btn-ghost" href="work.html">All works</a>
        </div>
        <div class="work-grid">
          <a class="work-card reveal" href="work-suzuki-fronx.html">
            <img src="assets/images/work-suzuki-fronx.jpg" alt="Suzuki Fronx campaign key visual" />
            <div class="work-card-body">
              <div class="tags"><span class="tag">Brand &amp; Communication</span></div>
              <h3>Suzuki All-new Fronx</h3>
              <p>Launching a new edge for Suzuki’s SUV story in Vietnam.</p>
            </div>
          </a>
          <a class="work-card reveal" href="work-ariston.html">
            <img src="assets/images/work-ariston.png" alt="Ariston Ice Challenge campaign visual" />
            <div class="work-card-body">
              <div class="tags"><span class="tag">Brand &amp; Communication</span></div>
              <h3>Ariston Ice Challenge</h3>
              <p>Trusted, but no longer talked about — until quality was felt again.</p>
            </div>
          </a>
          <a class="work-card reveal" href="work-mitsubishi.html">
            <img src="assets/images/brand-d-cubes.png" alt="Digital systems visual for Mitsubishi CDI" />
            <div class="work-card-body">
              <div class="tags"><span class="tag">Customer Experience &amp; CRM</span><span class="tag">Digital Solutions &amp; Innovation</span></div>
              <h3>Mitsubishi Motor Vietnam — CDI</h3>
              <p>Customer data integration from marketing through to dealer sales.</p>
            </div>
          </a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">Clients</p>
          <h2>Of course we think we’re great (we wrote this website).</h2>
          <p class="lead">For the real truth about our works, listen to our clients.</p>
        </div>
        <div class="quote-block reveal">
          <blockquote>“They don’t work like a typical agency; they work like they’re sitting in our office. If you’ve noticed Suzuki turning heads in Vietnam lately, DSquare is the team behind it.”</blockquote>
          <cite>Client perspective from the current DSQUARE website design</cite>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:0;">
      <div class="container">
        <div class="section-head row reveal">
          <div>
            <p class="eyebrow">Insights</p>
            <h2>Subscribe to our insights</h2>
            <p class="lead">Practical points of view from delivery — frameworks, project learnings, and operating notes across our four capabilities.</p>
          </div>
          <a class="btn btn-ghost" href="insights.html">All insights</a>
        </div>
        <div class="insight-grid">
          <a class="insight-feature reveal" href="insight-fragmented-operating-models.html">
            <img src="assets/images/bg-arcs.png" alt="" />
            <div class="body">
              <div class="meta"><span class="tag">Commerce</span><span class="tag">Customer Experience &amp; CRM</span></div>
              <h3>The hidden cost of fragmented digital operating models</h3>
              <p>When campaigns, ecommerce, CRM, and media don’t share an operating model, spend creates activity — not compounding value.</p>
            </div>
          </a>
          <div class="insight-list">
            <a class="insight-list-item reveal" href="insight-marketing-sales-loop.html">
              <div class="meta"><span class="tag">Digital Solutions &amp; Innovation</span><span class="tag">CX &amp; CRM</span></div>
              <h3>Closing the marketing-to-sales loop</h3>
              <p>What breaks when media, leads, and dealer sales don’t share one customer flow — and how to design the handoff.</p>
            </a>
            <a class="insight-list-item reveal" href="insight-brand-quality-proof.html">
              <div class="meta"><span class="tag">Brand &amp; Communication</span></div>
              <h3>When “quality” stops being felt</h3>
              <p>Project learning from demonstration-led brand proof.</p>
            </a>
          </div>
        </div>
      </div>
    </section>

    <section class="section-tight">
      <div class="container reveal">
        <div class="split">
          <div>
            <p class="eyebrow">Contact</p>
            <h2>We’ve talked enough about the work.</h2>
            <p class="lead">Let’s talk about your project.</p>
            <div class="btn-row"><a class="btn btn-amber" href="contact.html">Talk to us</a></div>
          </div>
          <div class="media-frame">
            <img src="assets/images/brand-d2-logo.png" alt="DSQUARE D2 mark" />
          </div>
        </div>
      </div>
    </section>
""",
)

files["services.html"] = page(
    "Services — DSQUARE",
    "DSQUARE services: Brand & Communication, Customer Experience & CRM, Commerce, and Digital Solutions & Innovation.",
    "services.html",
    f"""
    <section class="page-hero">
      <div class="container reveal">
        <p class="eyebrow">Services</p>
        <h1>What DSQUARE owns</h1>
        <p class="lead">Four capability pillars. Same names across the site. Each one states the proposition, the problems we solve, what we deliver, and the work and insights that prove it.</p>
      </div>
    </section>
    <section class="section" style="padding-top:0;">
      <div class="container">
{pillar("brand-communication", "01 · Brand & Communication", "Brand &amp; Communication",
    "So our daily battle is to survive the skip button. We work with you to strip away the corporate speak and craft stories people really want to see.",
    ["Familiar, but no longer exciting.", "Trusted, but no longer talked about — especially with younger audiences.", "Campaigns that lack local relevance or a reason to care."],
    ["Brand platform and positioning", "IMC campaign ideation and production", "Launch storytelling and content systems", "Experience-led brand demonstrations"],
    [("work-ariston.html", "Ariston Ice Challenge"), ("work-suzuki-fronx.html", "Suzuki All-new Fronx"), ("work-gojek.html", "Gojek — Achieve More")],
    [("insight-brand-quality-proof.html", "When quality stops being felt"), ("insight-fragmented-operating-models.html", "Fragmented digital operating models")])}
{pillar("cx-crm", "02 · Customer Experience & CRM", "Customer Experience &amp; CRM",
    "Growth doesn’t stop at awareness. We design journeys, CRM, and customer data flows so teams can care for customers faster — from lead to sales to loyalty.",
    ["Marketing data and dealer/sales data live apart.", "Leads stall between media, web, test-drive, and purchase.", "Loyalty programs lack a usable single customer view."],
    ["Customer journey design", "CRM and loyalty program design", "Lead-to-sales process design", "Customer data integration requirements"],
    [("work-mitsubishi.html", "Mitsubishi Motor Vietnam — CDI")],
    [("insight-marketing-sales-loop.html", "Closing the marketing-to-sales loop"), ("insight-fragmented-operating-models.html", "Fragmented digital operating models")])}
{pillar("commerce", "03 · Commerce", "Commerce",
    "Yep, we hate the hassle as much as you do. That’s why we turn your data into clear answers, building storefronts that just work. Our only goal is removing every barrier between intention and purchase.",
    ["Traffic arrives, but conversion paths are fragmented.", "Ecommerce, CRM, and media optimize in silos.", "Teams can’t see CAC → repeat → LTV as one loop."],
    ["Commerce experience design", "Conversion and catalog UX", "Data-led D2C operating model design", "Commerce storytelling tied to real outcomes"],
    [("work-gojek.html", "Gojek — Achieve More"), ("work-mitsubishi.html", "Mitsubishi Motor Vietnam — CDI")],
    [("insight-fragmented-operating-models.html", "Fragmented digital operating models")])}
{pillar("digital-solutions", "04 · Digital Solutions & Innovation", "Digital Solutions &amp; Innovation",
    "Agencies don’t solve problems with slides alone. We turn growth strategy into platforms, integrations, and digital products teams can operate.",
    ["Strategy exists, but delivery stacks can’t run it.", "Tools multiply without a shared data model.", "Brand, commerce, and customer data need one system path."],
    ["Solution architecture and integration", "Custom digital product builds", "Marketing-to-sales system design", "Innovation prototypes with an operating path"],
    [("work-mitsubishi.html", "Mitsubishi Motor Vietnam — CDI"), ("work-suzuki-fronx.html", "Suzuki All-new Fronx")],
    [("insight-marketing-sales-loop.html", "Closing the marketing-to-sales loop"), ("insight-fragmented-operating-models.html", "Fragmented digital operating models")])}
      </div>
    </section>
""",
)

files["work.html"] = page(
    "Work — DSQUARE",
    "Selected DSQUARE work across Brand & Communication, CX & CRM, Commerce, and Digital Solutions & Innovation.",
    "work.html",
    """
    <section class="page-hero with-visual">
      <div class="page-hero-bg" aria-hidden="true"><img src="assets/images/page-work-hero.png" alt="" /></div>
      <div class="container reveal">
        <p class="eyebrow">Work</p>
        <h1>The Work</h1>
        <p class="lead">Real business problems solved. Each case keeps Challenge / Solution / Impact — and states DSQUARE’s role, with links back to services and insights.</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="work-grid">
          <a class="work-card reveal" href="work-suzuki-fronx.html">
            <img src="assets/images/work-suzuki-fronx.jpg" alt="Suzuki Fronx" />
            <div class="work-card-body">
              <div class="tags"><span class="tag">Brand &amp; Communication</span></div>
              <h3>Suzuki All-new Fronx</h3>
              <p>Launching a new edge for Suzuki’s SUV story.</p>
            </div>
          </a>
          <a class="work-card reveal" href="work-ariston.html">
            <img src="assets/images/work-ariston.png" alt="Ariston" />
            <div class="work-card-body">
              <div class="tags"><span class="tag">Brand &amp; Communication</span></div>
              <h3>Ariston Ice Challenge</h3>
              <p>Trusted, but no longer talked about.</p>
            </div>
          </a>
          <a class="work-card reveal" href="work-mitsubishi.html">
            <img src="assets/images/brand-d-cubes.png" alt="Mitsubishi CDI" />
            <div class="work-card-body">
              <div class="tags"><span class="tag">Customer Experience &amp; CRM</span><span class="tag">Digital Solutions &amp; Innovation</span></div>
              <h3>Mitsubishi Motor Vietnam — CDI</h3>
              <p>Marketing-to-sales customer data integration.</p>
            </div>
          </a>
          <a class="work-card reveal" href="work-gojek.html">
            <img src="assets/images/bg-layers.png" alt="Gojek" />
            <div class="work-card-body">
              <div class="tags"><span class="tag">Brand &amp; Communication</span><span class="tag">Commerce</span></div>
              <h3>Gojek — Achieve More</h3>
              <p>Local-relevance campaign with published results.</p>
            </div>
          </a>
        </div>
      </div>
    </section>
""",
)


def case_page(filename, title, meta_desc, client, tags, hero_img, hero_alt, intro, challenge, solution, role, impact_html, services, insights, note=""):
    tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    svc = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in services)
    ins = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in insights)
    note_html = f'<p class="note-box">{note}</p>' if note else ""
    files[filename] = page(
        f"{title} — DSQUARE Work",
        meta_desc,
        "work.html",
        f"""
    <section class="page-hero with-visual case-hero">
      <div class="page-hero-bg" aria-hidden="true"><img src="{hero_img}" alt="" /></div>
      <div class="container reveal">
        <p class="eyebrow">Case study</p>
        <h1>{title}</h1>
        <p class="lead">{intro}</p>
        <div class="case-meta">{tag_html}<span class="tag tag-amber">{client}</span></div>
      </div>
    </section>
    <section class="section">
      <div class="container stack">
        <div class="media-frame reveal"><img src="{hero_img}" alt="{hero_alt}" style="aspect-ratio:21/9;object-fit:cover;" /></div>
        <div class="story-grid reveal">
          <div class="story-card"><h3>Challenge</h3><p>{challenge}</p></div>
          <div class="story-card"><h3>Solution</h3><p>{solution}</p></div>
          <div class="story-card"><h3>Impact</h3>{impact_html}</div>
        </div>
        <div class="role-panel reveal">
          <h2 class="mt-0" style="font-size:1.25rem;">DSQUARE’s Role</h2>
          <p class="mb-0" style="color:var(--text);">{role}</p>
        </div>
        {note_html}
        <div class="two-col reveal">
          <div class="aside-card"><h4>Related services</h4><ul>{svc}</ul></div>
          <div class="aside-card"><h4>Related insights</h4><ul>{ins}</ul></div>
        </div>
        <div class="btn-row reveal">
          <a class="btn btn-ghost" href="work.html">All work</a>
          <a class="btn btn-primary" href="contact.html">Talk about a similar brief</a>
        </div>
      </div>
    </section>
""",
    )


case_page(
    "work-suzuki-fronx.html",
    "Suzuki All-new Fronx",
    "DSQUARE Brand & Communication work for Suzuki All-new Fronx, featured in the current website design.",
    "Suzuki Vietnam",
    ["Brand &amp; Communication"],
    "assets/images/work-suzuki-fronx.jpg",
    "All-new Suzuki Fronx campaign key visual",
    "Launching a new edge for Suzuki Fronx — campaign-led creative that puts the model beyond every mold.",
    "A new SUV needs more than specs. It needs a distinctive edge in a crowded category conversation.",
    "A campaign-led visual system and launch narrative centered on Fronx as a break from category conventions — pairing product presence with a bold communication frame.",
    "DSQUARE’s current website design features this Fronx launch as Brand &amp; Communication work. This prototype presents the published creative surface and positioning; detailed scope beyond what is evidenced in the design file and public materials is not claimed here.",
    "<p>Qualitative signal from the design file: Fronx as a head-turning Suzuki presence in Vietnam. No sales or media KPIs are published for this case in source materials, so none are shown.</p>",
    [("services.html#brand-communication", "Brand &amp; Communication")],
    [("insight-brand-quality-proof.html", "When quality stops being felt"), ("insight-fragmented-operating-models.html", "Fragmented digital operating models")],
    "Evidence rule: no fabricated launch metrics.",
)

case_page(
    "work-ariston.html",
    "Ariston Ice Challenge",
    "DSQUARE Brand & Communication case study for Ariston Best Quality Ice Challenge with published engagement results.",
    "Ariston",
    ["Brand &amp; Communication"],
    "assets/images/work-ariston.png",
    "Ariston water heater frozen in ice challenge visual",
    "Trusted, but no longer talked about. We needed people to feel the quality again.",
    "Ariston had long been synonymous with quality water heaters, yet that reputation had stopped being felt — especially among younger consumers. The brand needed to refresh communication and reinforce “Best Quality.”",
    "Put product strength through an extreme demonstration: an Iceberg Challenge that makes quality visible and shareable — instead of restating the claim in corporate language.",
    "DSQUARE owned Brand &amp; Communication for the challenge concept and campaign storytelling: turning a quality claim into a live demonstration format and digital amplification of the proof moment.",
    """
    <div class="impact-grid" style="margin-top:.4rem;">
      <div class="impact-item"><div class="value">6k</div><p>views in 20 minutes of livestream</p><p class="note">Published on dsquare.com.vn</p></div>
      <div class="impact-item"><div class="value">+400%</div><p>page engagement increase</p><p class="note">Published on dsquare.com.vn</p></div>
      <div class="impact-item"><div class="value">Positive</div><p>user feedback on the demonstration</p><p class="note">As published</p></div>
    </div>
    """,
    [("services.html#brand-communication", "Brand &amp; Communication")],
    [("insight-brand-quality-proof.html", "When quality stops being felt")],
)

case_page(
    "work-mitsubishi.html",
    "Mitsubishi Motor Vietnam — Customer Data Integration",
    "DSQUARE CX/CRM and Digital Solutions case: marketing-to-sales customer data integration for Mitsubishi Motor Vietnam.",
    "Mitsubishi Motor Vietnam",
    ["Customer Experience &amp; CRM", "Digital Solutions &amp; Innovation"],
    "assets/images/brand-d-cubes.png",
    "Abstract systems visual representing data integration",
    "Streamlining customer data from advertising media and website visits to leads, test drives, and dealer sales.",
    "Marketing data from the Mitsubishi brand and sales data from dealers were disconnected. Without a single source managing media, leads, and sales, the brand could not streamline care or spot bottlenecks.",
    "A Customer Data Integration System designed to connect marketing-to-sales data across the journey — so teams can act faster and care for customers with a more complete view.",
    "DSQUARE delivered the customer data integration approach across Digital Solutions &amp; Innovation and Customer Experience &amp; CRM: defining the marketing-to-sales data flow and the operating intent for dealer-connected customer care.",
    "<p>Published outcome language: better ability to optimize efficiency, define bottlenecks, and care for customers faster. No numeric KPIs are published on the public project page.</p>",
    [("services.html#cx-crm", "Customer Experience &amp; CRM"), ("services.html#digital-solutions", "Digital Solutions &amp; Innovation")],
    [("insight-marketing-sales-loop.html", "Closing the marketing-to-sales loop"), ("insight-fragmented-operating-models.html", "Fragmented digital operating models")],
)

case_page(
    "work-gojek.html",
    "Gojek — Achieve More",
    "DSQUARE Brand & Communication case for Gojek Achieve More with published communication and business results.",
    "Gojek",
    ["Brand &amp; Communication", "Commerce"],
    "assets/images/bg-layers.png",
    "Abstract layered graphic for Gojek case study",
    "Enhance brand awareness and saliency for GoRide &amp; GoFood by building local relevance.",
    "Gojek had low awareness partly due to low local relevancy. In a growing food and ride-hailing market, the brand needed a culturally sharp role.",
    "A campaign idea inspired by the local proverb “Được voi đòi tiên” — creating strong local relevance while highlighting Gojek’s role in helping people achieve more.",
    "DSQUARE led Brand &amp; Communication for the Achieve More campaign platform and local-relevance storytelling connecting awareness work to service usage across GoRide and GoFood.",
    """
    <p>Published results (Apr–June 2021, dsquare.com.vn):</p>
    <div class="impact-grid" style="margin-top:.7rem;">
      <div class="impact-item"><div class="value">+~15%</div><p>Brand awareness</p></div>
      <div class="impact-item"><div class="value">+46%</div><p>GoFood completed orders (June)</p></div>
      <div class="impact-item"><div class="value">+4% / +1%</div><p>GoRide / GoFood market share</p></div>
    </div>
    <p class="note-box">Also published: ad recognition +8%, positive sentiment +4%, convenience imagery +13%, affordability +7%, new users +9.34% (May) / +40.13% (June), GoFood order frequency +32% (June).</p>
    """,
    [("services.html#brand-communication", "Brand &amp; Communication"), ("services.html#commerce", "Commerce")],
    [("insight-brand-quality-proof.html", "When quality stops being felt"), ("insight-fragmented-operating-models.html", "Fragmented digital operating models")],
)

files["insights.html"] = page(
    "Insights — DSQUARE",
    "DSQUARE insights on growth systems, brand proof, CRM, commerce, and digital operating models.",
    "insights.html",
    """
    <section class="page-hero">
      <div class="container reveal">
        <p class="eyebrow">Insights</p>
        <h1>Insights from the work</h1>
        <p class="lead">Categories follow the same four capabilities as Services and Work. These are delivery POVs and project learnings — not generic blog filler.</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="work-grid">
          <a class="work-card reveal" href="insight-fragmented-operating-models.html">
            <img src="assets/images/bg-arcs.png" alt="" />
            <div class="work-card-body">
              <div class="tags"><span class="tag">Commerce</span><span class="tag">CX &amp; CRM</span><span class="tag">Digital Solutions</span></div>
              <h3>Fragmented digital operating models</h3>
              <p>Why disconnected stacks fail to compound growth.</p>
            </div>
          </a>
          <a class="work-card reveal" href="insight-marketing-sales-loop.html">
            <img src="assets/images/brand-d-cubes.png" alt="" />
            <div class="work-card-body">
              <div class="tags"><span class="tag">Digital Solutions &amp; Innovation</span><span class="tag">CX &amp; CRM</span></div>
              <h3>Closing the marketing-to-sales loop</h3>
              <p>Design notes from customer data integration work.</p>
            </div>
          </a>
          <a class="work-card reveal" href="insight-brand-quality-proof.html">
            <img src="assets/images/work-ariston.png" alt="" />
            <div class="work-card-body">
              <div class="tags"><span class="tag">Brand &amp; Communication</span></div>
              <h3>When quality stops being felt</h3>
              <p>Demonstration-led proof for reputation decay.</p>
            </div>
          </a>
        </div>
      </div>
    </section>
""",
)


def insight_article(filename, title, desc, tags, author_role, author_note, hero, sections_html, services, work):
    tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    svc = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in services)
    wrk = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in work)
    files[filename] = page(
        f"{title} — DSQUARE Insights",
        desc,
        "insights.html",
        f"""
    <section class="page-hero">
      <div class="container reveal">
        <p class="eyebrow">Insight</p>
        <h1>{title}</h1>
        <div class="meta" style="margin-top:1rem;">{tag_html}</div>
      </div>
    </section>
    <section class="section" style="padding-top:1rem;">
      <div class="container article-layout">
        <article class="article-body reveal">
          <div class="media-frame" style="margin-bottom:1.4rem;"><img src="{hero}" alt="" style="aspect-ratio:16/9;object-fit:cover;" /></div>
          {sections_html}
        </article>
        <aside class="reveal">
          <div class="author-card">
            <img src="assets/images/team-portrait.jpg" alt="DSQUARE practitioner portrait" />
            <div>
              <strong class="text-white">DSQUARE</strong>
              <div style="color:var(--muted);font-size:.9rem;">{author_role}</div>
            </div>
          </div>
          <div class="aside-card">
            <h4>Expertise note</h4>
            <p style="margin:0;font-size:.92rem;">{author_note}</p>
          </div>
          <div class="aside-card"><h4>Related services</h4><ul>{svc}</ul></div>
          <div class="aside-card"><h4>Related work</h4><ul>{wrk}</ul></div>
        </aside>
      </div>
    </section>
""",
    )


insight_article(
    "insight-fragmented-operating-models.html",
    "The hidden cost of fragmented digital operating models",
    "DSQUARE POV on why disconnected ecommerce, CRM, and media stacks fail to compound growth value.",
    ["Commerce", "Customer Experience &amp; CRM", "Digital Solutions &amp; Innovation"],
    "Digital Growth practice",
    "Adapted from DSQUARE’s public Digital Growth point of view. No invented client metrics.",
    "assets/images/bg-arcs.png",
    """
    <p class="lead">Many brands invest heavily in digital, but those investments are rarely designed to work as a system.</p>
    <h2>The structural problem</h2>
    <p>Campaigns, ecommerce, CRM, and performance media often run on separate stacks — with different data models, metrics, and ownership. Over time, digital spend drives activity, but not compounding value. Customer data accumulates outside the brand’s core systems. ROI is optimized per channel, not across CAC → repeat → LTV.</p>
    <h2>Where the loop breaks</h2>
    <p>The disconnect between upper and lower funnel is an operating-model problem. When Brand &amp; Communication, Commerce, and Customer Experience &amp; CRM don’t share ownership and data contracts, every channel can “win” while the brand still fails to compound.</p>
    <h2>Design the system first</h2>
    <ol>
      <li>Start from strategy and operating model, not tool selection.</li>
      <li>Define shared customer objects and handoffs across media → site/app → CRM → sales/service.</li>
      <li>Measure lifecycle outcomes, not only channel dashboards.</li>
      <li>Then translate the model into platforms through Digital Solutions &amp; Innovation.</li>
    </ol>
    """,
    [("services.html#commerce", "Commerce"), ("services.html#cx-crm", "Customer Experience &amp; CRM"), ("services.html#digital-solutions", "Digital Solutions &amp; Innovation")],
    [("work-mitsubishi.html", "Mitsubishi CDI"), ("work-gojek.html", "Gojek — Achieve More")],
)

insight_article(
    "insight-marketing-sales-loop.html",
    "Closing the marketing-to-sales loop",
    "DSQUARE implementation insight on connecting media, leads, and dealer sales through customer data integration.",
    ["Digital Solutions &amp; Innovation", "Customer Experience &amp; CRM"],
    "CX / Digital delivery",
    "Grounded in the published Mitsubishi Motor Vietnam customer data integration brief. No invented KPIs.",
    "assets/images/brand-d-cubes.png",
    """
    <p class="lead">When marketing data and dealer sales data don’t meet, brands can’t see where the journey breaks — or care for customers fast enough.</p>
    <h2>What disintegration looks like</h2>
    <p>Media data, website visits, leads, test drives, and dealer sales often live in separate systems. The opportunity isn’t “more dashboards.” It’s one flow that makes bottlenecks visible.</p>
    <h2>A practical design sequence</h2>
    <ul>
      <li>Map the real handoffs: advertising → site → lead → test drive → sale.</li>
      <li>Name the owner of each handoff (brand marketing, CRM, dealer ops).</li>
      <li>Define the minimum shared customer fields that must travel with the journey.</li>
      <li>Build the integration so care teams can act — not only report.</li>
    </ul>
    <h2>Why this sits across two capabilities</h2>
    <p>Customer Experience &amp; CRM owns the journey and care intent. Digital Solutions &amp; Innovation owns the system that makes the loop operable. Naming both keeps the ask clear.</p>
    """,
    [("services.html#cx-crm", "Customer Experience &amp; CRM"), ("services.html#digital-solutions", "Digital Solutions &amp; Innovation")],
    [("work-mitsubishi.html", "Mitsubishi CDI")],
)

insight_article(
    "insight-brand-quality-proof.html",
    "When quality stops being felt: making proof experiential",
    "Project learning from demonstration-led brand communication, including Ariston Ice Challenge.",
    ["Brand &amp; Communication"],
    "Brand &amp; Communication practice",
    "Grounded in the published Ariston Ice Challenge brief and results. No extra metrics added.",
    "assets/images/work-ariston.png",
    """
    <p class="lead">A brand can remain trusted and still disappear from conversation. When quality is assumed, it stops being felt.</p>
    <h2>The reputation trap</h2>
    <p>Long-running quality leaders often keep the claim and lose the feeling — especially with younger audiences who didn’t live the original proof. Restating “best quality” rarely reopens attention.</p>
    <h2>Demonstration as strategy</h2>
    <p>The Ariston Ice Challenge reframed proof as experience: put the product through an extreme test, then let the demonstration travel. Published outcomes included 6k views in 20 minutes of livestream and a 400% page engagement increase.</p>
    <h2>A reusable brief question</h2>
    <p>What would make the claim undeniable in one shared moment — and how will Brand &amp; Communication carry that proof into ongoing content?</p>
    """,
    [("services.html#brand-communication", "Brand &amp; Communication")],
    [("work-ariston.html", "Ariston Ice Challenge"), ("work-suzuki-fronx.html", "Suzuki Fronx")],
)

files["about.html"] = page(
    "About DSQUARE",
    "About DSQUARE: Growth Partner Agency in Vietnam under Square Group.",
    "about.html",
    """
    <section class="page-hero">
      <div class="container reveal">
        <p class="eyebrow">About</p>
        <h1>DSQUARE</h1>
        <p class="lead">A Growth Partner Agency in Vietnam. Part of Square Group. We help brands grow through Brand &amp; Communication, Customer Experience &amp; CRM, Commerce, and Digital Solutions &amp; Innovation.</p>
      </div>
    </section>
    <section class="section">
      <div class="container split reveal">
        <div class="stack">
          <p class="voice-line">Wild ideas, but flawless execution. Fast delivery, but never sloppy.</p>
          <p>That’s the standard clients describe. We work like we’re sitting in the brand’s office — pairing creative sharpness with the systems that make growth repeatable.</p>
          <div class="detail-box">
            <h4>Legal entity</h4>
            <p>Square Direct Advertising Company Limited (DSQUARE). Public materials also reference CÔNG TY TNHH QUẢNG CÁO TRỰC TIẾP BÌNH PHƯƠNG.</p>
          </div>
          <div class="detail-box">
            <h4>Leadership</h4>
            <p>Vu Nguyen, CEO — public profile notes experience in marketing and advertising including Toyota Vietnam and JWT Vietnam, with a focus on brand building.</p>
          </div>
          <div class="btn-row">
            <a class="btn btn-primary" href="services.html">What we do</a>
            <a class="btn btn-ghost" href="contact.html">Contact</a>
          </div>
        </div>
        <div class="media-frame">
          <img src="assets/images/team-portrait.jpg" alt="DSQUARE team member portrait" />
        </div>
      </div>
    </section>
""",
)

files["contact.html"] = page(
    "Contact DSQUARE",
    "Contact DSQUARE in Ho Chi Minh City about Brand & Communication, CX & CRM, Commerce, or Digital Solutions.",
    "contact.html",
    """
    <section class="page-hero">
      <div class="container reveal">
        <p class="eyebrow">Contact</p>
        <h1>Let’s talk about your project</h1>
        <p class="lead">Happy to just send another brief &amp; run — or sit down and unpack the growth problem first.</p>
      </div>
    </section>
    <section class="section">
      <div class="container contact-panel">
        <div class="contact-facts reveal">
          <div class="fact"><strong>Work inquiries</strong><a href="mailto:thework@dsquare.com.vn">thework@dsquare.com.vn</a></div>
          <div class="fact"><strong>Office</strong><span>54-56 Hoa Dao, Ward 2, Phu Nhuan Dist, Ho Chi Minh City, Vietnam</span></div>
          <div class="fact"><strong>Telephone</strong><span>(84-28) 3517 3635</span></div>
          <div class="fact"><strong>Capability focus</strong><span>Tell us which pillar you think you need — Brand &amp; Communication, CX &amp; CRM, Commerce, or Digital Solutions &amp; Innovation.</span></div>
        </div>
        <form class="reveal" data-contact-form>
          <div class="form-grid">
            <div class="form-row">
              <label>Name<input name="name" required placeholder="Your name" /></label>
              <label>Email<input type="email" name="email" required placeholder="you@company.com" /></label>
            </div>
            <label>Company<input name="company" placeholder="Brand or company" /></label>
            <label>Capability focus
              <select name="capability">
                <option>Brand &amp; Communication</option>
                <option>Customer Experience &amp; CRM</option>
                <option>Commerce</option>
                <option>Digital Solutions &amp; Innovation</option>
                <option>Not sure yet</option>
              </select>
            </label>
            <label>A few words about your project*
              <textarea name="project" required placeholder="What are you trying to grow, fix, or launch?"></textarea>
            </label>
            <button class="btn btn-primary" type="submit">Send message</button>
            <p data-form-status hidden class="note-box"></p>
          </div>
        </form>
      </div>
    </section>
""",
)

# Remove obsolete meta insight filename if present
old = ROOT / "insight-challenge-to-system.html"
if old.exists():
    old.unlink()

files["aeo-review.html"] = page(
    "AEO Review — DSQUARE Prototype",
    "Final recommended AEO/GEO changes for the DSQUARE website prototype, for Strategy and Design review.",
    "aeo-review.html",
    """
    <section class="page-hero">
      <div class="container reveal">
        <p class="eyebrow">Strategy + Design review</p>
        <h1>AEO / GEO Review</h1>
        <p class="lead">Final recommended state of the prototype: what stayed faithful to Figma, what evolved for Growth Partner positioning and answer-engine clarity, and what was cut because it felt like a redesign, SaaS filler, or fabricated proof.</p>
        <div class="aeo-legend">
          <span class="chip chip-kept">Kept from Figma</span>
          <span class="chip chip-modified">Modified</span>
          <span class="chip chip-added">Added for AEO/GEO</span>
          <span class="chip chip-removed">Removed / avoided</span>
        </div>
        <div class="btn-row">
          <a class="btn btn-primary" href="index.html">Open homepage</a>
          <a class="btn btn-ghost" href="services.html">Open services</a>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:0;">
      <div class="container">
        <div class="review-block reveal">
          <h3>Review verdict</h3>
          <p style="margin:0;">The prototype should read as an <strong style="color:var(--text);">evolution of the current Figma</strong> — campaign-led, dark, sharp, and opinionated — not a generic growth-SaaS reskin. AEO improvements are structural (entity, taxonomy, role, linking, evidence discipline), while voice and visual hierarchy stay close to the file.</p>
        </div>

        <div class="review-block reveal">
          <h3>1. Kept from Figma (do not lose these)</h3>
          <ul>
            <li>Campaign-led homepage hero using Suzuki Fronx KV as the dominant full-bleed visual.</li>
            <li>Dark base, electric blue accents, amber highlights from brand imagery.</li>
            <li>Work storytelling: Challenge / Solution / Impact.</li>
            <li>Distinctive voice lines: “We prefer to let the work run the show,” “We fuse sharp ideas…,” commerce/brand service personality, client quote, large DSQUARE footer wordmark.</li>
            <li>Core pages and assets from the design file (hero, work, case, services energy, contact).</li>
          </ul>
        </div>

        <div class="review-block reveal">
          <h3>2. Modified (evolution, not redesign)</h3>
          <ul>
            <li><strong>Hero copy:</strong> restored campaign headline (“Launching a new edge for Suzuki Fronx”) and placed the Growth Partner positioning as explicit supporting text — instead of a SaaS-style invented H1.</li>
            <li><strong>UI chrome:</strong> reduced pill buttons, glow, and feature-card SaaS patterning; sharper editorial capability rows closer to agency craft.</li>
            <li><strong>Services:</strong> reorganized around the four Growth Partner pillars, written in Figma voice rather than template blurbs.</li>
            <li><strong>Work tags:</strong> real capability names only; Suzuki tagged to Brand &amp; Communication based on evidenced creative surface (no over-claimed second pillar).</li>
            <li><strong>Hero contrast:</strong> stronger left scrim plus an amber-ruled positioning panel so Growth Partner copy stays readable over campaign photography.</li>
          </ul>
        </div>

        <div class="review-block reveal">
          <h3>3. Added for AEO / GEO</h3>
          <ul>
            <li>Explicit entity statement: <em>DSQUARE is a Growth Partner Agency in Vietnam</em> + four capabilities in visible text.</li>
            <li>Consistent capability taxonomy across Home, Services, Work, Insights, Contact, Footer.</li>
            <li>“DSQUARE’s Role” on every case study.</li>
            <li>First-class Insights module with capability categories and expertise attribution.</li>
            <li>Bidirectional Service ↔ Work ↔ Insights linking.</li>
            <li>Evidence discipline: published metrics only (Ariston, Gojek); unpublished cases state that plainly.</li>
          </ul>
        </div>

        <div class="review-block reveal">
          <h3>4. Removed / avoided</h3>
          <ul>
            <li>Lorem ipsum, “[Text: …]” placeholders, Rayo template leftovers.</li>
            <li>Invented homepage stat tiles and unsourced KPIs.</li>
            <li>Meta “page purpose” chips on public pages (review notes live here instead).</li>
            <li>Strategy-doc labels on the live site (“Entity”, “Capability gateway”, “not generic SEO posts”).</li>
            <li>Self-referential AEO explainer article; replaced with a delivery insight on marketing-to-sales loops.</li>
            <li>Generic SaaS headline “Growth systems brands can run on.”</li>
          </ul>
        </div>

        <h2 class="reveal" style="margin-top:2.5rem;">Change log for Strategy &amp; Design</h2>
        <table class="aeo-table reveal">
          <thead>
            <tr><th>Area</th><th>Status</th><th>Final recommendation</th><th>Why</th></tr>
          </thead>
          <tbody>
            <tr>
              <td>Campaign-led hero visual</td>
              <td><span class="status status-kept">Kept</span></td>
              <td>Full-bleed Fronx KV remains the first-viewport visual plane.</td>
              <td>Preserves strongest Figma move; brand still signaled with large DSQUARE lockup.</td>
            </tr>
            <tr>
              <td>Hero headline</td>
              <td><span class="status status-modified">Modified</span></td>
              <td>Use campaign line from the file; positioning sits under it in plain language.</td>
              <td>Keeps campaign energy while making who/what answerable for AEO.</td>
            </tr>
            <tr>
              <td>Growth Partner positioning</td>
              <td><span class="status status-added">Added</span></td>
              <td>Visible on Home, About, Footer, and meta descriptions.</td>
              <td>Entity clarity without rewriting brand personality.</td>
            </tr>
            <tr>
              <td>Four-capability taxonomy</td>
              <td><span class="status status-added">Added</span></td>
              <td>Brand &amp; Communication · CX &amp; CRM · Commerce · Digital Solutions &amp; Innovation</td>
              <td>Clear service categories; same labels everywhere.</td>
            </tr>
            <tr>
              <td>Visual system</td>
              <td><span class="status status-modified">Modified</span></td>
              <td>Sharper radii, less glow/pills, editorial capability layout.</td>
              <td>Pulls away from generic SaaS while staying dark/blue/amber.</td>
            </tr>
            <tr>
              <td>Brand voice</td>
              <td><span class="status status-kept">Kept</span></td>
              <td>Restore Figma/service personality lines; cut brochure filler.</td>
              <td>Voice is part of brand distinctiveness for GEO.</td>
            </tr>
            <tr>
              <td>Case studies</td>
              <td><span class="status status-modified">Modified</span></td>
              <td>Keep Challenge/Solution/Impact; add Role; link services/insights; publish-only metrics.</td>
              <td>Proof objects become attributable and trustworthy.</td>
            </tr>
            <tr>
              <td>Insights</td>
              <td><span class="status status-added">Added</span></td>
              <td>Three expertise pieces aligned to capabilities, with authors and related work.</td>
              <td>Demonstrates first-hand expertise instead of SEO blogging.</td>
            </tr>
            <tr>
              <td>Internal linking</td>
              <td><span class="status status-added">Added</span></td>
              <td>Service ↔ Work ↔ Insights on every major template.</td>
              <td>Builds the topical graph answer engines need.</td>
            </tr>
            <tr>
              <td>Fabricated facts</td>
              <td><span class="status status-removed">Removed</span></td>
              <td>No invented stats; Suzuki role carefully scoped to evidenced creative surface.</td>
              <td>Protects trust for Strategy review and GEO citations.</td>
            </tr>
            <tr>
              <td>Public “page purpose” labels</td>
              <td><span class="status status-removed">Removed</span></td>
              <td>Moved review commentary into this AEO Review page only.</td>
              <td>Keeps public pages brand-first, not process-first.</td>
            </tr>
          </tbody>
        </table>

        <div class="review-block reveal" style="margin-top:2rem;">
          <h3>Page map</h3>
          <ul>
            <li><a href="index.html">Home</a> — campaign hero + positioning + what we do + work + insights teaser</li>
            <li><a href="services.html">Services</a> — four pillars with proposition / problems / capabilities / work / insights</li>
            <li><a href="work.html">Work</a> + Suzuki / Ariston / Mitsubishi / Gojek cases</li>
            <li><a href="insights.html">Insights</a> + 3 articles</li>
            <li><a href="about.html">About</a> · <a href="contact.html">Contact</a></li>
          </ul>
        </div>

        <div class="review-block reveal">
          <h3>Open questions for Strategy / Design (not fabricated answers)</h3>
          <ul>
            <li>Confirm official role wording for Suzuki Fronx beyond the creative surface shown in Figma.</li>
            <li>Confirm whether partner logo row should return once approved mark set is available.</li>
            <li>Confirm Insights author attribution format (named practitioners vs practice byline).</li>
            <li>Confirm contact email canonical: <code>thework@dsquare.com.vn</code> (from design) vs other public addresses.</li>
          </ul>
        </div>
      </div>
    </section>
""",
)

for name, html in files.items():
    (ROOT / name).write_text(html, encoding="utf8")
    print("wrote", name)

print("done", len(files))
