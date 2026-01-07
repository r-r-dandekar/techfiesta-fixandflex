import { useEffect } from "react";

export default function Home() {
  useEffect(() => {
    // Inject Framer scripts if needed later
  }, []);

  return (
    <div
      dangerouslySetInnerHTML={{
        __html: `
<!-- START FRAMER PAGE -->
<div id="main">
  <div class="framer-J1zB5 framer-6rg2se">
    
    <!-- NAVBAR -->
    <nav class="framer-q1LIA framer-1bbq23v">
      <div class="framer-1aqw7tj">
        <div class="framer-e3m6kx">
          <h3 class="framer-text">FixAndFlex</h3>
        </div>
        <button class="framer-text">Get Started</button>
      </div>
    </nav>

    <!-- HERO -->
    <section style="padding:120px 0; text-align:center;">
      <h1 class="framer-text" style="font-size:56px;">
        AI Powered Loan Recommendation
      </h1>
      <p class="framer-text" style="margin-top:20px;">
        Smarter lending decisions using intelligent financial rules
      </p>
      <button style="margin-top:40px;">Check Eligibility</button>
    </section>

    <!-- FEATURES -->
    <section style="padding:80px 0;">
      <div style="display:flex; gap:40px; justify-content:center;">
        <div>✔ FOIR Based Approval</div>
        <div>✔ Income Floor Rules</div>
        <div>✔ Explainable AI</div>
      </div>
    </section>

    <!-- FOOTER -->
    <footer style="padding:40px; opacity:0.7;">
      © 2026 FixAndFlex
    </footer>

  </div>
</div>
<!-- END FRAMER PAGE -->
        `,
      }}
    />
  );
}
