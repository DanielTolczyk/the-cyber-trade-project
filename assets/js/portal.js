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
    }
  };

  let tooltipEl = null;
  let activeTermEl = null;
  let hideTimeout = null;

  function createTooltipElement() {
    tooltipEl = document.createElement("div");
    tooltipEl.className = "glossary-tooltip-card";
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

        span.addEventListener("mouseenter", (e) => showTooltip(e.target, match));
        span.addEventListener("mouseleave", hideTooltip);
        span.addEventListener("click", (e) => {
          e.stopPropagation();
          showTooltip(e.target, match);
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
      initNavigation();
      initMobileSidebar();
      initResponsiveTables();
    });
  } else {
    initGlossaryParser();
    initDiagramLightbox();
    initGlossarySearch();
    initNavigation();
    initMobileSidebar();
    initResponsiveTables();
  }
})();

