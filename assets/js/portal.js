/**
 * The Cybersecurity Trade Project - Interactive Portal Engine
 * Features:
 * 1. Automatic Glossary Term Parsing & Floating Tooltip Cards.
 * 2. Active Sidebar Navigation Tracking.
 */

(function () {
  "use strict";

  const GLOSSARY_TERMS = {
    "Taft-Hartley": {
      title: "Taft-Hartley Act (LMRA § 302(c))",
      category: "Labor Statute",
      def: "Federal labor statute permitting jointly trusteed, multi-employer training and benefit funds co-governed by equal labor and employer trustees to fund $0 tuition apprenticeships.",
      citation: "29 U.S.C. § 186(c)"
    },
    "Taft-Hartley Act": {
      title: "Taft-Hartley Act (LMRA § 302(c))",
      category: "Labor Statute",
      def: "Federal labor statute permitting jointly trusteed, multi-employer training and benefit funds co-governed by equal labor and employer trustees to fund $0 tuition apprenticeships.",
      citation: "29 U.S.C. § 186(c)"
    },
    "ERISA": {
      title: "ERISA (§ 403 Fiduciary Shield)",
      category: "Federal Law",
      def: "Employee Retirement Income Security Act. Guarantees that pooled health and pension funds are legally insulated from employer bankruptcy, creditors, and corporate lawsuits.",
      citation: "29 U.S.C. § 1103"
    },
    "JATC": {
      title: "Joint Apprenticeship & Training Committee",
      category: "Skilled Trade",
      def: "Bipartisan trust body representing labor and participating employers that oversees classroom instruction (RTI), cyber ranges, and apprentice logbook verification.",
      citation: "Pillar VI / 29 CFR Part 29"
    },
    "DOL": {
      title: "U.S. Department of Labor (29 CFR 29)",
      category: "Regulatory Body",
      def: "Federal agency governing Registered Apprenticeship Programs, unlocking WIOA workforce grants and employer tax credits on Day 1 without new legislation.",
      citation: "National Apprenticeship Act"
    },
    "Master of Record": {
      title: "Master of Record (MoR)",
      category: "Licensure Tier",
      def: "A licensed Master Practitioner holding legal and statutory sign-off authority for enterprise security baselines and standing to file formal Notices of Safety Non-Concurrence.",
      citation: "Pillar IV & Pillar V"
    },
    "MoR": {
      title: "Master of Record (MoR)",
      category: "Licensure Tier",
      def: "A licensed Master Practitioner holding legal and statutory sign-off authority for enterprise security baselines and standing to file formal Notices of Safety Non-Concurrence.",
      citation: "Pillar IV & Pillar V"
    },
    "Journeyman": {
      title: "Licensed Journeyman",
      category: "Licensure Tier",
      def: "A licensed practitioner who has completed 8,000 verified operational logbook hours, passed the practical challenge examination, and possesses autonomous practice rights.",
      citation: "Pillar IV / 100% RJPB"
    },
    "RJPB": {
      title: "Regional Journeyman Prevailing Baseline",
      category: "Labor Economics",
      def: "The local prevailing hourly wage baseline for Journeymen, upon which apprentice wage steps (50% Tier 1 to 80% Tier 4) are strictly pegged.",
      citation: "Governance / Wage Scales"
    },
    "PLA": {
      title: "Prior Learning Assessment (PLA)",
      category: "Grandfathering",
      def: "Standardized evaluation awarding direct runtime hours and Related Technical Instruction (RTI) credits for documented career experience and accredited coursework.",
      citation: "Pillar I & Transition Plan"
    },
    "WIOA": {
      title: "Workforce Innovation & Opportunity Act",
      category: "Workforce Grant",
      def: "Federal statutory program providing non-debt training subsidies and equipment grants to community colleges and registered apprenticeship sponsors.",
      citation: "WIOA Title I"
    },
    "CUAAC": {
      title: "Cyber Underwriting & Actuarial Consortium",
      category: "Insurance",
      def: "Consortium of primary cyber underwriters establishing standardized 25% to 35% premium warranty discount schedules for compliant skilled trade staffing ratios.",
      citation: "Pillar VII"
    },
    "RTI": {
      title: "Related Technical Instruction (RTI)",
      category: "Workforce Training",
      def: "The mandatory, paid 20% classroom, lab, and simulation instruction (minimum 144 hours/year) completed alongside on-the-job operational runtime.",
      citation: "Pillar II & 29 CFR Part 29"
    },
    "AMF": {
      title: "Annual Maintenance Fee (AMF)",
      category: "Credentialism",
      def: "Recurring commercial certification vendor subscription fees charged annually, strictly prohibited from trade licensure renewals ($0 triennial renewal).",
      citation: "Pillar IV / Anti-Credentialism"
    },
    "Career Runtime": {
      title: "Career Runtime Hours",
      category: "Trade Telemetry",
      def: "Total verified hands-on operational hours logged in active defensive, administrative, engineering, or incident triage roles, distinct from passive study.",
      citation: "Pillar III & Logbook Standards"
    },
    "W-2": {
      title: "W-2 Direct Employment",
      category: "Labor Classification",
      def: "Direct salaried or hourly employment with statutory worker protections, mandatory overtime rules, and employer tax withholding, as distinct from 1099 contracts.",
      citation: "Pillar II"
    },
    "SE-APP": {
      title: "Application Security (SE-APP)",
      category: "Specialty Track",
      def: "A Tier 1 discipline specialty endorsement covering secure architecture, automated CI/CD security tooling, software supply-chain defenses, and SBOM lifecycles.",
      citation: "Specialty Track Specification"
    },
    "SE-MED": {
      title: "Medical Device Security (SE-MED)",
      category: "Specialty Track",
      def: "A Tier 2 statutory life-safety specialty endorsement (+20% to +25% wage adder) governing embedded firmware (SiMD), SaMD, mobile health apps, and FDA 524B compliance.",
      citation: "Specialty Track Specification"
    },
    "Cyber Civil Defense Reserve": {
      title: "Cyber Civil Defense Reserve (CCDR)",
      category: "Workforce Buffer",
      def: "A counter-cyclical public workforce mechanism deploying unabsorbed apprentices during economic downturns to protect municipal infrastructure and schools funded by public grants.",
      citation: "Governance / Guild Charter"
    },
    "CCDR": {
      title: "Cyber Civil Defense Reserve (CCDR)",
      category: "Workforce Buffer",
      def: "A counter-cyclical public workforce mechanism deploying unabsorbed apprentices during economic downturns to protect municipal infrastructure and schools funded by public grants.",
      citation: "Governance / Guild Charter"
    },
    "FOIA": {
      title: "Final-Offer Interest Arbitration (FOIA)",
      category: "Labor Dispute",
      def: "Compulsory, binding tripartite arbitration resolving contract deadlocks at Tier-I Critical Infrastructure facilities within 14 days, with zero strike risk or defensive standdowns.",
      citation: "Governance / Guild Charter"
    },
    "Final-Offer Interest Arbitration": {
      title: "Final-Offer Interest Arbitration (FOIA)",
      category: "Labor Dispute",
      def: "Compulsory, binding tripartite arbitration resolving contract deadlocks at Tier-I Critical Infrastructure facilities within 14 days, with zero strike risk or defensive standdowns.",
      citation: "Governance / Guild Charter"
    },
    "Hardware-Enforced Cryptographic Pulse": {
      title: "Hardware Cryptographic Pulse",
      category: "Telemetry Integrity",
      def: "Physical FIDO2/WebAuthn capacitive touch user presence requirement contextually bound to privileged actions, defeating synthetic bot telemetry and ghost-worker staffing.",
      citation: "Universal Logbook Schema"
    },
    "OOB-HMS": {
      title: "Out-of-Band Hardware Enclave Multi-Sig",
      category: "Supply Chain",
      def: "Threshold multi-signature release gate for Tier-I infrastructure held across isolated hardware security keys operated by Master and Journeyman engineers, decoupled from public CAs.",
      citation: "Velocity, Cloud & Safe Harbor"
    },
    "Fallback Statutory Mandate Bridge": {
      title: "Fallback Statutory Mandate Bridge",
      category: "Regulatory Safeguard",
      def: "Automated transition shifting trade enforcement from private cyber insurance underwriting into mandatory federal procurement (FAR/DFARS) and PUC utility covenants if private capacity falls.",
      citation: "Pillar VII & Transition Plan"
    },
    "Strict Blast-Radius Localization Rule": {
      title: "Strict Blast-Radius Localization Rule",
      category: "Cloud Governance",
      def: "Cloud force majeure rule limiting toll-free compliance suspensions strictly to documented CSP sub-regions/services (72-hr max), preventing fraudulent tenant-parking abuse.",
      citation: "Velocity, Cloud & Safe Harbor"
    },
    "72-Hour Internal Remediation Rule": {
      title: "72-Hour Internal Remediation Rule",
      category: "Ethics & Whistleblower",
      def: "Mandatory corporate cure period requiring a Form FORM-003 filing before external whistleblower bounties attach, preventing malicious compliance traps.",
      citation: "Code of Ethics & Conduct"
    },
    "Statutory Malpractice Liability Cap": {
      title: "Statutory Malpractice Liability Cap",
      category: "Liability Shield",
      def: "$0 personal civil damages liability cap for non-negligent Masters of Record and Journeymen maintaining verified baseline compliance and clean attestation feeds.",
      citation: "Pillar V & Technical Refusal"
    },
    "Tier-I Critical Infrastructure No-Disruption Covenant": {
      title: "Tier-I No-Disruption Covenant",
      category: "Public Safety",
      def: "Statutory covenant legally binding cybersecurity personnel defending Tier-I infrastructure against labor stoppages or walkouts, routing bargaining deadlocks to FOIA.",
      citation: "Governance / Guild Charter"
    },
    "FORM-005": {
      title: "Targeted OSS Exemption (FORM-005)",
      category: "Procedural Form",
      def: "Standardized instrument executed by a Master of Record certifying an internal security fork and active compensating controls for an unpatched open-source dependency (90-day grace period).",
      citation: "Templates / FORM-005"
    },
    "OSS Orphan Vulnerability": {
      title: "OSS Orphan Vulnerability Protocol",
      category: "Supply Chain",
      def: "Protocol allowing teams to create isolated security forks and runtime compensating controls under MoR certification when upstream open-source packages have unpatched zero-days.",
      citation: "Velocity, Cloud & Safe Harbor"
    }
  };

  let tooltipEl = null;
  let activeTermEl = null;
  let hideTimeout = null;

  function createTooltipElement() {
    tooltipEl = document.createElement("div");
    tooltipEl.className = "glossary-tooltip-card";
    tooltipEl.id = "glossary-tooltip-card";
    tooltipEl.setAttribute("role", "tooltip");
    tooltipEl.setAttribute("aria-live", "polite");
    tooltipEl.innerHTML = `
      <div class="tooltip-header">
        <span class="tooltip-title" id="tt-title"></span>
        <span class="tooltip-category" id="tt-cat"></span>
      </div>
      <div class="tooltip-body" id="tt-body"></div>
      <div class="tooltip-citation" id="tt-cite"></div>
    `;
    document.body.appendChild(tooltipEl);

    tooltipEl.addEventListener("mouseenter", () => clearTimeout(hideTimeout));
    tooltipEl.addEventListener("mouseleave", hideTooltip);
  }

  function showTooltip(targetEl, termKey) {
    const data = GLOSSARY_TERMS[termKey];
    if (!data || !tooltipEl) return;
    clearTimeout(hideTimeout);
    activeTermEl = targetEl;

    document.getElementById("tt-title").textContent = data.title;
    document.getElementById("tt-cat").textContent = data.category;
    document.getElementById("tt-body").textContent = data.def;
    document.getElementById("tt-cite").textContent = data.citation;

    const rect = targetEl.getBoundingClientRect();
    const tooltipWidth = 320;
    let left = rect.left + window.scrollX + (rect.width / 2) - (tooltipWidth / 2);
    let top = rect.bottom + window.scrollY + 8;

    if (left < 16) left = 16;
    if (left + tooltipWidth > window.innerWidth - 16) {
      left = window.innerWidth - tooltipWidth - 16;
    }

    tooltipEl.style.left = `${left}px`;
    tooltipEl.style.top = `${top}px`;
    tooltipEl.classList.add("active");
  }

  function hideTooltip() {
    hideTimeout = setTimeout(() => {
      if (tooltipEl) tooltipEl.classList.remove("active");
      activeTermEl = null;
    }, 120);
  }


  function initGlossaryParser() {
    const article = document.querySelector(".portal-article");
    if (!article) return;
    createTooltipElement();

    const sortedTerms = Object.keys(GLOSSARY_TERMS).sort((a, b) => b.length - a.length);
    const regexPattern = new RegExp(`\\b(${sortedTerms.map(t => t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|")})\\b`, "g");

    const walker = document.createTreeWalker(
      article,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function (node) {
          const parent = node.parentElement;
          if (!parent) return NodeFilter.FILTER_REJECT;
          const tag = parent.tagName.toLowerCase();
          if (["pre", "code", "a", "h1", "h2", "h3", "h4", "script", "style"].includes(tag)) {
            return NodeFilter.FILTER_REJECT;
          }
          if (parent.classList.contains("glossary-term")) {
            return NodeFilter.FILTER_REJECT;
          }
          return NodeFilter.FILTER_ACCEPT;
        }
      }
    );

    const nodesToReplace = [];
    while (walker.nextNode()) {
      const node = walker.currentNode;
      if (regexPattern.test(node.nodeValue)) {
        nodesToReplace.push(node);
      }
    }

    nodesToReplace.forEach(node => {
      const fragment = document.createDocumentFragment();
      let lastIndex = 0;
      const text = node.nodeValue;

      text.replace(regexPattern, (match, p1, offset) => {
        if (offset > lastIndex) {
          fragment.appendChild(document.createTextNode(text.substring(lastIndex, offset)));
        }
        const span = document.createElement("span");
        span.className = "glossary-term";
        span.textContent = match;
        span.setAttribute("data-term", match);
        span.tabIndex = 0;
        span.setAttribute("role", "button");
        span.setAttribute("aria-describedby", "glossary-tooltip-card");

        span.addEventListener("mouseenter", (e) => showTooltip(e.target, match));
        span.addEventListener("mouseleave", hideTooltip);
        span.addEventListener("focus", (e) => showTooltip(e.target, match));
        span.addEventListener("blur", hideTooltip);
        span.addEventListener("click", (e) => {
          e.stopPropagation();
          showTooltip(e.target, match);
        });
        span.addEventListener("keydown", (e) => {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            showTooltip(e.target, match);
          } else if (e.key === "Escape") {
            hideTooltip();
          }
        });

        fragment.appendChild(span);
        lastIndex = offset + match.length;
      });

      if (lastIndex < text.length) {
        fragment.appendChild(document.createTextNode(text.substring(lastIndex)));
      }
      node.parentNode.replaceChild(fragment, node);
    });

    document.addEventListener("click", (e) => {
      if (!e.target.closest(".glossary-term") && !e.target.closest(".glossary-tooltip-card")) {
        hideTooltip();
      }
    });
  }

  // Diagram Lightbox / Modal Zoom Engine
  function initDiagramLightbox() {
    const preBlocks = document.querySelectorAll(".portal-article pre");
    if (!preBlocks.length) return;

    // Create Modal Elements
    const modal = document.createElement("div");
    modal.className = "diagram-modal-overlay";
    modal.innerHTML = `
      <div class="diagram-modal-container">
        <div class="diagram-modal-header">
          <span class="diagram-modal-title">Blueprint & Architectural Diagram</span>
          <button class="diagram-modal-close" type="button">Close &times;</button>
        </div>
        <div class="diagram-modal-body">
          <pre><code id="diagram-modal-code"></code></pre>
        </div>
      </div>
    `;
    document.body.appendChild(modal);

    const modalCode = document.getElementById("diagram-modal-code");
    const closeBtn = modal.querySelector(".diagram-modal-close");

    function openModal(codeContent) {
      modalCode.textContent = codeContent;
      modal.classList.add("active");
      document.body.style.overflow = "hidden";
    }

    function closeModal() {
      modal.classList.remove("active");
      document.body.style.overflow = "";
    }

    closeBtn.addEventListener("click", closeModal);
    modal.addEventListener("click", (e) => {
      if (e.target === modal) closeModal();
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && modal.classList.contains("active")) closeModal();
    });

    // Attach Expand Buttons to Diagrams
    preBlocks.forEach(pre => {
      const code = pre.querySelector("code");
      const text = code ? code.textContent : pre.textContent;

      // Only attach if it contains ASCII box-drawing characters
      if (text.includes("┌") || text.includes("+─") || text.includes("│") || text.includes("├")) {
        pre.classList.add("diagram-interactive");

        const expandBtn = document.createElement("button");
        expandBtn.className = "diagram-expand-btn";
        expandBtn.type = "button";
        expandBtn.innerHTML = "<span>Expand ↗</span>";
        expandBtn.addEventListener("click", (e) => {
          e.stopPropagation();
          openModal(text);
        });

        pre.style.position = "relative";
        pre.appendChild(expandBtn);

        pre.addEventListener("click", () => {
          openModal(text);
        });
      }
    });
  }

  // Glossary Live Search & Filter
  function initGlossarySearch() {
    const isGlossaryPage = window.location.pathname.includes("GLOSSARY") || document.title.includes("Glossary");
    if (!isGlossaryPage) return;

    const article = document.querySelector(".portal-article");
    if (!article) return;

    const searchWrap = document.createElement("div");
    searchWrap.className = "glossary-search-container";
    searchWrap.innerHTML = `
      <input type="text" id="glossary-search-input" class="glossary-search-box" placeholder="Filter terms & acronyms (e.g., DOL, Taft-Hartley, ERISA, MoR, RJPB)..." />
      <span class="glossary-count" id="glossary-term-count"></span>
    `;

    const firstH2 = article.querySelector("h2");
    if (firstH2) {
      firstH2.parentNode.insertBefore(searchWrap, firstH2);
    } else {
      article.insertBefore(searchWrap, article.firstChild);
    }

    const searchInput = document.getElementById("glossary-search-input");
    const countEl = document.getElementById("glossary-term-count");
    const listItems = article.querySelectorAll("ul li");

    countEl.textContent = `${listItems.length} terms cataloged`;

    searchInput.addEventListener("input", (e) => {
      const query = e.target.value.toLowerCase().trim();
      let matchCount = 0;

      listItems.forEach(li => {
        const text = li.textContent.toLowerCase();
        if (!query || text.includes(query)) {
          li.style.display = "";
          matchCount++;
        } else {
          li.style.display = "none";
        }
      });

      countEl.textContent = query ? `${matchCount} matching` : `${listItems.length} terms cataloged`;
    });
  }

  function initMobileSidebar() {
    const toggleBtn = document.getElementById("btn-toggle-sidebar");
    const closeBtn = document.getElementById("btn-close-sidebar");
    const sidebar = document.getElementById("portal-sidebar");
    const backdrop = document.getElementById("portal-sidebar-backdrop");

    const openSidebar = () => {
      if (sidebar) sidebar.classList.add("open");
      if (backdrop) backdrop.classList.add("active");
      document.body.style.overflow = "hidden";
    };

    const closeSidebar = () => {
      if (sidebar) sidebar.classList.remove("open");
      if (backdrop) backdrop.classList.remove("active");
      document.body.style.overflow = "";
    };

    if (toggleBtn) toggleBtn.addEventListener("click", openSidebar);
    if (closeBtn) closeBtn.addEventListener("click", closeSidebar);
    if (backdrop) backdrop.addEventListener("click", closeSidebar);

    // Auto-close when clicking any link in mobile drawer
    const sidebarLinks = sidebar ? sidebar.querySelectorAll("a") : [];
    sidebarLinks.forEach(link => {
      link.addEventListener("click", () => {
        if (window.innerWidth <= 900) {
          closeSidebar();
        }
      });
    });
  }

  function initResponsiveTables() {
    const tables = document.querySelectorAll(".portal-article table");
    tables.forEach(table => {
      if (!table.parentElement.classList.contains("table-scroll-wrapper")) {
        const wrapper = document.createElement("div");
        wrapper.className = "table-scroll-wrapper";
        table.parentNode.insertBefore(wrapper, table);
        wrapper.appendChild(table);
      }
    });
  }

  // Secure Client-Side Static In-Memory Search Engine
  function initGlobalSearch() {
    const searchBtn = document.getElementById("btn-portal-search");
    const backdrop = document.getElementById("portal-search-backdrop");
    const input = document.getElementById("portal-search-input");
    const closeBtn = document.getElementById("portal-search-close-btn");
    const resultsContainer = document.getElementById("portal-search-results");
    if (!backdrop || !input || !resultsContainer) return;

    let searchIndex = null;
    let selectedIndex = -1;
    let currentResults = [];

    function getSiteBaseUrl() {
      const scriptEl = document.querySelector('script[src*="portal.js"]');
      if (scriptEl) {
        const src = scriptEl.getAttribute("src") || "";
        const idx = src.indexOf("/assets/js/portal.js");
        if (idx !== -1) {
          const base = src.substring(0, idx);
          return base.endsWith("/") ? base : (base ? base + "/" : "/");
        }
      }
      if (typeof window !== "undefined" && window.location.pathname.startsWith("/framework")) {
        return "/framework/";
      }
      return "/";
    }

    const baseUrl = getSiteBaseUrl();

    // Device & OS Shortcut Detection
    function detectShortcutLabel() {
      const isTouch = window.matchMedia("(pointer: coarse)").matches || ("ontouchstart" in window);
      const kbd = document.querySelector(".search-btn-kbd");
      if (!kbd) return;

      if (isTouch || window.innerWidth <= 768) {
        kbd.style.display = "none";
        return;
      }

      const platform = (navigator.userAgentData?.platform || navigator.platform || navigator.userAgent || "").toLowerCase();
      const isMac = /mac|iphone|ipad|ipod/.test(platform);
      const shortcutText = isMac ? "⌘K" : "Ctrl+K";
      kbd.textContent = shortcutText;

      if (searchBtn) {
        searchBtn.setAttribute("aria-label", `Search Framework (${shortcutText})`);
      }
    }

    detectShortcutLabel();
    window.addEventListener("resize", detectShortcutLabel);

    async function loadSearchIndex() {
      if (searchIndex && searchIndex.length) return searchIndex;
      try {
        const fetchUrl = `${baseUrl}assets/js/search-index.json`;
        const res = await fetch(fetchUrl);
        searchIndex = res.ok ? await res.json() : [];
      } catch (err) {
        searchIndex = [];
      }
      return searchIndex;
    }

    // Pre-fetch search index in background immediately for instant readiness
    loadSearchIndex();

    function openSearchModal() {
      backdrop.style.display = "flex";
      backdrop.setAttribute("aria-hidden", "false");
      if (searchBtn) searchBtn.setAttribute("aria-expanded", "true");
      document.body.style.overflow = "hidden";
      loadSearchIndex().then(() => renderSearchResults(input.value));
      setTimeout(() => input.focus(), 50);
    }

    function closeSearchModal() {
      backdrop.style.display = "none";
      backdrop.setAttribute("aria-hidden", "true");
      if (searchBtn) searchBtn.setAttribute("aria-expanded", "false");
      document.body.style.overflow = "";
      input.value = "";
      selectedIndex = -1;
      currentResults = [];
    }

    function sanitizeNavigationUrl(url, base) {
      if (!url) return "#";
      const raw = String(url).trim();
      if (/^(javascript|data|vbscript):/i.test(raw)) {
        return "#";
      }
      if (raw.startsWith("https://") || raw.startsWith("http://")) {
        return raw;
      }
      return (base || "/") + raw.replace(/^\//, "");
    }

    function appendHighlightedText(parent, text, tokens) {
      if (!tokens || !tokens.length || !text) {
        parent.textContent = text || "";
        return;
      }
      const escaped = tokens.filter(t => t.length > 1).map(t => t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));
      if (!escaped.length) {
        parent.textContent = text;
        return;
      }
      const regex = new RegExp(`(${escaped.join("|")})`, "gi");
      let lastIdx = 0;
      text.replace(regex, (match, p1, offset) => {
        if (offset > lastIdx) {
          parent.appendChild(document.createTextNode(text.substring(lastIdx, offset)));
        }
        const mark = document.createElement("mark");
        mark.className = "search-highlight";
        mark.textContent = match;
        parent.appendChild(mark);
        lastIdx = offset + match.length;
      });
      if (lastIdx < text.length) {
        parent.appendChild(document.createTextNode(text.substring(lastIdx)));
      }
    }

    function getContextSnippet(content, tokens, maxLen = 180) {
      if (!content) return "";
      if (!tokens.length) return content.slice(0, maxLen) + (content.length > maxLen ? "..." : "");
      const lower = content.toLowerCase();
      let firstMatch = -1;
      for (const t of tokens) {
        const idx = lower.indexOf(t);
        if (idx !== -1 && (firstMatch === -1 || idx < firstMatch)) firstMatch = idx;
      }
      if (firstMatch === -1) return content.slice(0, maxLen) + (content.length > maxLen ? "..." : "");
      const start = Math.max(0, firstMatch - 45);
      const end = Math.min(content.length, start + maxLen);
      let snip = content.substring(start, end).trim();
      if (start > 0) snip = "..." + snip;
      if (end < content.length) snip = snip + "...";
      return snip;
    }

    function renderSearchResults(rawQuery) {
      while (resultsContainer.firstChild) resultsContainer.removeChild(resultsContainer.firstChild);

      const sanitized = (rawQuery || "").toLowerCase().replace(/[^\w\s\-\.\:\/]/g, "").slice(0, 64).trim();
      const rawTokens = sanitized.split(/\s+/).filter(Boolean);
      
      const tokens = [];
      rawTokens.forEach(t => {
        tokens.push(t);
        if (t.endsWith("ies") && t.length > 4) tokens.push(t.slice(0, -3) + "y");
        else if (t.endsWith("es") && t.length > 4) tokens.push(t.slice(0, -2));
        else if (t.endsWith("s") && t.length > 3) tokens.push(t.slice(0, -1));
        if (t.endsWith("ing") && t.length > 5) tokens.push(t.slice(0, -3));
        if (t.endsWith("ed") && t.length > 4) tokens.push(t.slice(0, -2));
      });

      if (!rawTokens.length) {
        currentResults = (searchIndex || []).slice(0, 8);
      } else {
        const scored = [];
        (searchIndex || []).forEach(item => {
          const docTitle = (item.docTitle || item.title || "").toLowerCase();
          const heading = (item.heading || "").toLowerCase();
          const cat = (item.category || "").toLowerCase();
          const content = (item.content || item.snippet || "").toLowerCase();

          let score = 0;
          let matchedTokensCount = 0;

          if (heading.includes(sanitized)) score += 150;
          else if (docTitle.includes(sanitized)) score += 120;
          else if (content.includes(sanitized)) score += 60;

          rawTokens.forEach(t => {
            let tokenHit = false;
            if (heading.includes(t)) { score += 70; tokenHit = true; }
            if (docTitle.includes(t)) { score += 40; tokenHit = true; }
            if (cat.includes(t)) { score += 25; tokenHit = true; }
            
            let contentHits = 0;
            let pos = content.indexOf(t);
            while (pos !== -1 && contentHits < 6) {
              contentHits++;
              score += 15;
              pos = content.indexOf(t, pos + t.length);
            }
            if (contentHits > 0) tokenHit = true;
            if (tokenHit) matchedTokensCount++;
          });

          if (rawTokens.length > 1 && matchedTokensCount === rawTokens.length) {
            score += 50;
          }

          if (score > 0) {
            scored.push({ item, score });
          }
        });

        scored.sort((a, b) => b.score - a.score);
        currentResults = scored.slice(0, 15).map(s => s.item);
      }

      if (!currentResults.length) {
        const noResults = document.createElement("div");
        noResults.className = "portal-search-no-results";
        noResults.textContent = `No framework specifications found matching "${sanitized}".`;
        resultsContainer.appendChild(noResults);
        return;
      }

      selectedIndex = 0;
      currentResults.forEach((item, idx) => {
        const link = document.createElement("a");
        link.className = `portal-search-result-item ${idx === selectedIndex ? "selected" : ""}`;
        link.href = sanitizeNavigationUrl(item.url, baseUrl);

        const headerDiv = document.createElement("div");
        headerDiv.className = "portal-search-result-header";

        const titleSpan = document.createElement("span");
        titleSpan.className = "portal-search-result-title";
        appendHighlightedText(titleSpan, item.docTitle || item.title, rawTokens);

        const catSpan = document.createElement("span");
        catSpan.className = "portal-search-result-category";
        catSpan.textContent = item.category;

        headerDiv.appendChild(titleSpan);
        headerDiv.appendChild(catSpan);
        link.appendChild(headerDiv);

        if (item.heading && item.heading !== (item.docTitle || item.title)) {
          const sectionDiv = document.createElement("div");
          sectionDiv.className = "portal-search-result-section";
          sectionDiv.appendChild(document.createTextNode("§ "));
          appendHighlightedText(sectionDiv, item.heading, rawTokens);
          link.appendChild(sectionDiv);
        }

        const snippetP = document.createElement("p");
        snippetP.className = "portal-search-result-snippet";
        const snippetText = getContextSnippet(item.content || item.snippet || "", rawTokens);
        appendHighlightedText(snippetP, snippetText, rawTokens);
        link.appendChild(snippetP);

        link.addEventListener("mouseenter", () => updateSelectedResult(idx));
        link.addEventListener("click", () => closeSearchModal());
        resultsContainer.appendChild(link);
      });
    }

    function updateSelectedResult(newIdx) {
      const items = resultsContainer.querySelectorAll(".portal-search-result-item");
      if (!items.length) return;
      selectedIndex = Math.max(0, Math.min(newIdx, items.length - 1));
      items.forEach((item, idx) => {
        if (idx === selectedIndex) {
          item.classList.add("selected");
          item.scrollIntoView({ block: "nearest" });
        } else {
          item.classList.remove("selected");
        }
      });
    }

    if (searchBtn) searchBtn.addEventListener("click", openSearchModal);
    if (closeBtn) closeBtn.addEventListener("click", closeSearchModal);
    backdrop.addEventListener("click", (e) => { if (e.target === backdrop) closeSearchModal(); });
    input.addEventListener("input", (e) => renderSearchResults(e.target.value));

    input.addEventListener("keydown", (e) => {
      if (e.key === "ArrowDown") {
        e.preventDefault();
        updateSelectedResult(selectedIndex + 1);
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        updateSelectedResult(selectedIndex - 1);
      } else if (e.key === "Enter") {
        e.preventDefault();
        const items = resultsContainer.querySelectorAll(".portal-search-result-item");
        if (items[selectedIndex]) items[selectedIndex].click();
      } else if (e.key === "Escape") {
        e.preventDefault();
        closeSearchModal();
      }
    });

    document.addEventListener("keydown", (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        backdrop.style.display === "flex" ? closeSearchModal() : openSearchModal();
      } else if (e.key === "Escape" && backdrop.style.display === "flex") {
        closeSearchModal();
      }
    });
  }

  function initNavigation() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll(".nav-item a");
    navLinks.forEach(link => {
      const href = link.getAttribute("href");
      if (href && (currentPath.endsWith(href) || (href === "./" && (currentPath.endsWith("/") || currentPath.endsWith("index.html"))))) {
        link.parentElement.classList.add("active");
        const parentDetails = link.closest("details");
        if (parentDetails) {
          parentDetails.open = true;
        }
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
      initGlossaryParser();
      initDiagramLightbox();
      initGlossarySearch();
      initGlobalSearch();
      initNavigation();
      initMobileSidebar();
      initResponsiveTables();
    });
  } else {
    initGlossaryParser();
    initDiagramLightbox();
    initGlossarySearch();
    initGlobalSearch();
    initNavigation();
    initMobileSidebar();
    initResponsiveTables();
  }
})();

