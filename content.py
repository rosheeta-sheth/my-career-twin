"""Static panel content for About, Resume, and Projects tabs."""

from pathlib import Path

LINKEDIN_URL = "https://www.linkedin.com/in/rosheeta-sheth/"
CONTACT_EMAIL = "rsheth48@gatech.edu"
RESUME_FILE = "RosheetaResume.pdf"

PROJECTS = [
    {
        "name": "ExpenseBot (AI Receipt & Expense Tracker)",
        "file": "expensebot.md",
        "summary": "Full-stack expense tracker integrating Cloud Vision OCR and Claude to auto-extract and categorize receipt data.",
        "tags": ["React", "Flask", "SQLAlchemy", "Claude API"],
    },
    {
        "name": "Personal Career Agent",
        "file": "personal_career_agent.html",
        "summary": "Agentic AI 'digital twin' chatbot grounded in personal career documents with real-time streaming.",
        "tags": ["Agentic AI", "Python", "OpenAI API", "Gradio"],
    },
    {
        "name": "AI Equity Traders (Multi-Agent System)",
        "file": "ai_equity_traders.html",
        "summary": "Autonomous multi-agent equity-trading simulation using MCP for real-time market data.",
        "tags": ["OpenAI Agents SDK", "MCP", "Python", "Gradio"],
    },
    {
        "name": "Multi-Agent Engineering Team",
        "file": "multi_agent_engineering_team.html",
        "summary": "Collaborative software 'engineering team' of role-based agents that build and test Python applications.",
        "tags": ["CrewAI", "Python", "Autonomous Agents"],
    },
    {
        "name": "DishRadar",
        "file": "dishradar.html",
        "summary": "Data analytics and aggregation project focused on dining and food trends.",
        "tags": ["Data Analytics", "GitHub", "Python"],
    },
    {
        "name": "Energy Consumption ML",
        "file": "energy_ml_project.pdf",
        "summary": "Machine learning models to analyze and predict energy usage patterns.",
        "tags": ["Python", "Scikit-learn", "Regression"],
    },
    {
        "name": "Time Series Forecasting",
        "file": "time_series_project.pdf",
        "summary": "Forecasting pipeline for sequential data with evaluation and visualization.",
        "tags": ["Time Series", "Forecasting", "Analytics"],
    },
    {
        "name": "Word Embeddings (Word2Vec)",
        "file": "word2vec_project.pdf",
        "summary": "NLP project exploring semantic relationships using word embedding techniques.",
        "tags": ["NLP", "Word2Vec", "Text Analytics"],
    },
    {
        "name": "Behavior Analysis",
        "file": "behavior_analysis_project.pdf",
        "summary": "Data-driven analysis of behavioral patterns from structured event data.",
        "tags": ["Analytics", "Python", "Visualization"],
    },
    {
        "name": "Emissions Analysis",
        "file": "emissions_analysis_project.pdf",
        "summary": "Environmental data analysis to quantify and interpret emissions trends.",
        "tags": ["Sustainability", "Data Analysis", "Reporting"],
    },
    {
        "name": "Simio Simulation",
        "file": "simio_project.pdf",
        "summary": "Discrete-event simulation for process optimization and capacity planning.",
        "tags": ["Simulation", "Operations", "Industrial Engineering"],
    },
]


def _project_cards() -> str:
    cards = []
    base_dir = Path(__file__).parent
    for project in PROJECTS:
        pdf_path = (base_dir / "detailed_projects" / project["file"]).resolve()
        href = f"/gradio_api/file={pdf_path}" if pdf_path.exists() else "#"
        tags = "".join(f"<span>{tag}</span>" for tag in project["tags"])
        cards.append(
            f"""
            <article class="project-card">
              <h3>{project["name"]}</h3>
              <p>{project["summary"]}</p>
              <div class="tag-row">{tags}</div>
              <a class="project-link" href="{href}" target="_blank" rel="noopener noreferrer">
                View project brief ↗
              </a>
            </article>
            """
        )
    return "\n".join(cards)


ABOUT_HTML = f"""
<section class="info-panel">
  <h2>About Rosheeta</h2>
  <p class="lead">
    Rosheeta Sheth is an Industrial Engineering student at the <strong>Georgia Institute of Technology</strong>, minoring in
    FinTech. She combines strategic product vision with hands-on technical execution, specializing in <strong>Agentic AI, Machine Learning, and Data Analytics</strong>. Her unique background equips her to seamlessly integrate engineering, data science, and product management to deliver impactful solutions.
  </p>
  <div class="info-grid">
    <div class="info-card">
      <h3>Professional Focus</h3>
      <ul>
        <li><strong>AI & ML Engineering:</strong> Building autonomous multi-agent systems, conversational digital twins, and robust ML/NLP models (OpenAI SDK, CrewAI, LangChain).</li>
        <li><strong>Data Science & Analytics:</strong> Transforming complex data into actionable insights using time-series forecasting, statistical modeling, and data visualization.</li>
        <li><strong>Product Management & Operations:</strong> Translating business requirements into technical architectures, optimizing processes, and delivering user-centric AI products.</li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Beyond the Data</h3>
      <ul>
        <li>Based in Atlanta, GA.</li>
        <li>Passionate about food, cooking, and culinary creativity.</li>
        <li>Currently developing a cookbook website and food-focused content platform to share her recipes and dining analytics.</li>
      </ul>
    </div>
  </div>
  <div class="info-cta">
    <a href="{LINKEDIN_URL}" target="_blank" rel="noopener noreferrer">Connect on LinkedIn</a>
    <a href="mailto:{CONTACT_EMAIL}">Send an email</a>
  </div>
</section>
"""

RESUME_HTML = f"""
<section class="info-panel">
  <h2>Resume Highlights</h2>
  <p class="lead">
    Industrial Engineering @ Georgia Tech · FinTech minor · Proven track record architecting complex AI, ML, and analytics solutions.
  </p>
  <div class="info-grid">
    <div class="info-card">
      <h3>Education</h3>
      <p><strong>Georgia Institute of Technology</strong></p>
      <p>B.S. Industrial Engineering · Minor in FinTech</p>
    </div>
    <div class="info-card">
      <h3>Technical Skills</h3>
      <ul>
        <li><strong>AI & LLMs:</strong> OpenAI API, CrewAI, MCP, LangChain, Agentic Frameworks, Prompt Engineering</li>
        <li><strong>Programming & Data:</strong> Python, SQL, Git/GitHub, Pandas, Scikit-Learn</li>
        <li><strong>Analytics & Visualization:</strong> Tableau, PowerBI, Time Series Forecasting, Regression, Data Modeling</li>
        <li><strong>Operations:</strong> Simio Simulation, Process Optimization, Capacity Planning</li>
      </ul>
    </div>
  </div>
  <p class="panel-note">
    Ask the chat assistant for role-specific details, project deep-dives, or how Rosheeta's
    background perfectly maps to your team.
  </p>
  <div class="info-cta">
    <a href="/gradio_api/file={(Path(__file__).parent / RESUME_FILE).resolve()}" target="_blank" rel="noopener noreferrer">Open full resume (PDF) ↗</a>
  </div>
</section>
"""

PROJECTS_HTML = f"""
<section class="info-panel">
  <h2>Selected Projects</h2>
  <p class="lead">
    A comprehensive portfolio of hands-on technical work spanning Agentic AI, Machine Learning, NLP, Simulation, and advanced Analytics.
  </p>
  <div class="project-grid">
    {_project_cards()}
  </div>
  <p class="panel-note">
    Use the Chat tab to ask how any project was built, what tools were used, or what outcomes were achieved.
  </p>
</section>
"""
