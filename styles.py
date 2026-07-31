"""Visual styling for Rosheeta's career chatbot."""

from content import CONTACT_EMAIL, LINKEDIN_URL

EXAMPLES = [
    "Tell me about your background and experience.",
    "Which AI and machine-learning projects have you built?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

HEADER_HTML = f"""
<header class="site-header" id="site-header">
  <div class="header-main">
    <div class="brand">
      <div class="avatar" aria-hidden="true">RS</div>
      <div class="brand-text">
        <h1>Rosheeta Sheth</h1>
        <p class="brand-subtitle">Industrial Engineering · Georgia Tech · FinTech minor</p>
        <p class="brand-tagline">Career assistant — ask about experience, skills, and projects</p>
      </div>
    </div>
    <div class="header-actions">
      <a class="header-link" href="{LINKEDIN_URL}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
      <a class="header-link" href="mailto:{CONTACT_EMAIL}">Email</a>
    </div>
  </div>
</header>
"""

CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {
  --bg: #0f1117;
  --surface: rgba(23, 25, 35, 0.6);
  --surface-2: rgba(30, 33, 43, 0.8);
  --border: rgba(255, 255, 255, 0.1);
  --border-strong: rgba(255, 255, 255, 0.2);
  --text: #f8fafc;
  --muted: #94a3b8;
  --accent: #8b5cf6;
  --accent-soft: rgba(139, 92, 246, 0.15);
  --accent-hover: #a78bfa;
  --user-bg: rgba(56, 189, 248, 0.15);
  --user-border: rgba(56, 189, 248, 0.3);
  --success: #10b981;
  --warning: #f59e0b;
  --danger: #ef4444;
  --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 10px 30px -5px rgba(0, 0, 0, 0.5);
  --radius: 12px;
  --radius-lg: 16px;
  --header-expanded: 118px;
  --header-compact: 56px;
}

html,
body,
gradio-app {
  background: var(--bg) !important;
  background-image: 
    radial-gradient(at 0% 0%, rgba(139, 92, 246, 0.15) 0px, transparent 50%),
    radial-gradient(at 100% 0%, rgba(56, 189, 248, 0.15) 0px, transparent 50%),
    radial-gradient(at 100% 100%, rgba(16, 185, 129, 0.1) 0px, transparent 50%) !important;
  background-attachment: fixed !important;
}

footer,
.built-with,
.show-api,
.api-docs {
  display: none !important;
}

.gradio-container {
  width: 100% !important;
  max-width: 920px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 20px 16px 28px !important;
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
}

.gradio-container *,
.gradio-container *::before,
.gradio-container *::after {
  box-sizing: border-box;
  min-width: 0;
}

.block,
.form {
  box-shadow: none !important;
}

/* ----------------------------- Header */
.site-header {
  margin-bottom: 12px;
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  background: var(--surface);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: var(--shadow-sm);
  overflow: hidden;
  transition: border-radius 220ms ease, box-shadow 220ms ease;
}

.header-main {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 16px 18px;
  transition: padding 220ms ease;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  min-width: 0;
}

.avatar {
  width: 40px;
  height: 40px;
  flex: 0 0 40px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  background: var(--accent);
  color: #fff;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.04em;
  transition: width 220ms ease, height 220ms ease, flex-basis 220ms ease;
}

.brand-text h1 {
  margin: 0 !important;
  color: var(--text) !important;
  font-size: 18px !important;
  font-weight: 700 !important;
  line-height: 1.25 !important;
  letter-spacing: -0.02em !important;
}

.brand-subtitle,
.brand-tagline {
  margin: 2px 0 0;
  color: var(--muted);
  font-size: 13px;
  line-height: 1.4;
  transition: opacity 180ms ease, max-height 220ms ease, margin 220ms ease;
}

.brand-tagline {
  font-size: 12px;
}

.header-actions {
  display: flex;
  gap: 8px;
  flex-shrink: 0;
}

.header-link {
  display: inline-flex;
  align-items: center;
  min-height: 34px;
  padding: 0 12px;
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--text);
  background: var(--surface-2);
  text-decoration: none;
  font-size: 12px;
  font-weight: 600;
  transition: border-color 140ms ease, color 140ms ease, background 140ms ease;
}

.header-link:hover {
  border-color: var(--accent);
  color: var(--accent);
  background: var(--accent-soft);
}

body.chat-active .site-header {
  border-radius: 10px;
}

body.chat-active .header-main {
  padding: 10px 14px;
}

body.chat-active .avatar {
  width: 32px;
  height: 32px;
  flex-basis: 32px;
  font-size: 11px;
  border-radius: 8px;
}

body.chat-active .brand-text h1 {
  font-size: 15px !important;
}

body.chat-active .brand-subtitle {
  opacity: 0;
  max-height: 0;
  margin: 0;
  overflow: hidden;
}

body.chat-active .brand-tagline {
  display: none;
}

/* ----------------------------- Tabs */
.main-tabs {
  margin-top: 0 !important;
}

.main-tabs > .tab-nav,
.main-tabs .tab-nav,
.main-tabs [role="tablist"] {
  gap: 4px !important;
  padding: 4px !important;
  margin-bottom: 12px !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
  background: var(--surface) !important;
  box-shadow: var(--shadow-sm) !important;
}

.main-tabs button[role="tab"],
.main-tabs .tab-nav button {
  min-height: 36px !important;
  padding: 0 14px !important;
  border: 0 !important;
  border-radius: 7px !important;
  background: transparent !important;
  color: var(--muted) !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  box-shadow: none !important;
  transform: none !important;
}

.main-tabs button[role="tab"][aria-selected="true"],
.main-tabs .tab-nav button.selected {
  background: var(--accent-soft) !important;
  color: var(--accent) !important;
}

.main-tabs button[role="tab"]:hover,
.main-tabs .tab-nav button:hover {
  color: var(--text) !important;
  background: var(--surface-2) !important;
  transform: none !important;
}

/* ----------------------------- Chat shell */
#chat-shell {
  gap: 10px !important;
}

#chat-toolbar {
  align-items: center !important;
  gap: 10px !important;
  margin: 0 !important;
}

#status-wrap {
  flex: 1 1 auto !important;
  border: 0 !important;
  background: transparent !important;
}

.chat-status {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  color: var(--muted);
  font-size: 12px;
  font-weight: 500;
}

.status-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--success);
}

.chat-status[data-state="thinking"] {
  color: var(--warning);
}

.chat-status[data-state="thinking"] .status-dot {
  background: var(--warning);
  animation: status-pulse 1.1s ease-in-out infinite;
}

.chat-status[data-state="error"] {
  color: var(--danger);
}

.chat-status[data-state="error"] .status-dot {
  background: var(--danger);
}

@keyframes status-pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.45; transform: scale(0.85); }
}

#new-chat {
  min-height: 34px !important;
  padding: 0 12px !important;
  font-size: 12px !important;
  white-space: nowrap !important;
}

/* ----------------------------- Buttons */
button {
  border-radius: 9px !important;
  border: 1px solid var(--border) !important;
  background: var(--surface) !important;
  color: var(--text) !important;
  box-shadow: none !important;
  font-family: Inter, ui-sans-serif, sans-serif !important;
  font-weight: 600 !important;
  transition: border-color 140ms ease, background 140ms ease, color 140ms ease !important;
}

button:hover {
  border-color: var(--border-strong) !important;
  color: var(--text) !important;
  transform: none !important;
}

#send-btn,
button.primary,
button[variant="primary"] {
  min-height: 46px !important;
  padding: 0 18px !important;
  border-color: var(--accent) !important;
  background: var(--accent) !important;
  color: #fff !important;
}

#send-btn:hover,
button.primary:hover,
button[variant="primary"]:hover {
  border-color: var(--accent-hover) !important;
  background: var(--accent-hover) !important;
  color: #fff !important;
}

/* ----------------------------- Chat */
#twin-chat,
#twin-chat.chatbot,
#twin-chat.chatbot.block {
  height: min(56vh, 520px) !important;
  min-height: 320px !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-lg) !important;
  background: var(--surface) !important;
  backdrop-filter: blur(20px) !important;
  -webkit-backdrop-filter: blur(20px) !important;
  box-shadow: var(--shadow-md) !important;
  overflow: hidden !important;
}

#twin-chat > .block-label,
#twin-chat > label,
#twin-chat .label-wrap,
#twin-chat .block-label,
#twin-chat > .label-container {
  display: none !important;
}

#twin-chat .placeholder,
#twin-chat .placeholder * {
  color: var(--muted) !important;
}

#twin-chat .message-row,
#twin-chat .message-row > *,
#twin-chat .message-row .role,
#twin-chat .message-row .message-wrap,
#twin-chat .message-row .bubble-wrap,
#twin-chat .message-row :is(.message, .message-bubble, .bubble) {
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
}

#twin-chat .message-row {
  padding: 5px 16px !important;
  margin: 0 !important;
  animation: message-in 280ms ease-out both;
}

#twin-chat .message-row:first-child {
  padding-top: 14px !important;
}

#twin-chat .message-row:last-child {
  padding-bottom: 14px !important;
}

@keyframes message-in {
  from {
    opacity: 0;
    transform: translateY(6px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

#twin-chat .message-row :is(.message, .message-bubble, .bubble):not(:has(:is(.message, .message-bubble, .bubble))) {
  width: fit-content !important;
  max-width: min(72ch, 88%) !important;
  padding: 11px 14px !important;
  border-radius: 14px !important;
  font-size: 14px !important;
  line-height: 1.6 !important;
  word-break: normal !important;
  overflow-wrap: break-word !important;
  white-space: pre-wrap !important;
}

#twin-chat .message-row.bot-row :is(.message, .message-bubble, .bubble):not(:has(:is(.message, .message-bubble, .bubble))),
#twin-chat .message-row[data-role="assistant"] :is(.message, .message-bubble, .bubble):not(:has(:is(.message, .message-bubble, .bubble))) {
  margin-right: auto !important;
  border: 1px solid var(--border) !important;
  background: var(--surface-2) !important;
  color: var(--text) !important;
}

#twin-chat .message-row.user-row :is(.message, .message-bubble, .bubble):not(:has(:is(.message, .message-bubble, .bubble))),
#twin-chat .message-row[data-role="user"] :is(.message, .message-bubble, .bubble):not(:has(:is(.message, .message-bubble, .bubble))) {
  margin-left: auto !important;
  border: 1px solid var(--user-border) !important;
  background: var(--user-bg) !important;
  color: var(--text) !important;
}

#twin-chat .message-row.user-row button,
#twin-chat .message-row[data-role="user"] button {
  display: none !important;
}

#twin-chat .message-row :is(.message, .message-bubble, .bubble) * {
  border: 0 !important;
  background: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}

#twin-chat .message-row p,
#twin-chat .message-row ul,
#twin-chat .message-row ol {
  margin-top: 0 !important;
  margin-bottom: 8px !important;
  word-break: normal !important;
  overflow-wrap: break-word !important;
}

#twin-chat .message-row p:last-child,
#twin-chat .message-row ul:last-child,
#twin-chat .message-row ol:last-child {
  margin-bottom: 0 !important;
}

#twin-chat .message-row strong,
#twin-chat .message-row b {
  font-weight: 700 !important;
  color: var(--text) !important;
}

#twin-chat .message-row ul,
#twin-chat .message-row ol {
  padding-left: 1.25rem !important;
}

#twin-chat .message-row li {
  margin-bottom: 4px !important;
}

#twin-chat .message-row a {
  color: var(--accent) !important;
  text-decoration: underline !important;
  text-underline-offset: 2px;
}

#twin-chat .message-row a:hover {
  color: var(--accent-hover) !important;
}

#twin-chat .icon-button,
#twin-chat button.icon-button {
  min-height: 26px !important;
  padding: 4px !important;
  border: 0 !important;
  color: var(--muted) !important;
  background: transparent !important;
  opacity: 0.5;
}

#twin-chat .message-row:hover .icon-button,
#twin-chat button.icon-button:hover {
  color: var(--accent) !important;
  opacity: 1;
}

/* Typing indicator injected by JS */
#twin-chat .typing-row {
  animation: message-in 220ms ease-out both;
}

#twin-chat .typing-bubble {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 12px 14px;
  border: 1px solid var(--border);
  border-radius: 14px;
  background: var(--surface-2);
}

#twin-chat .typing-bubble span {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--muted);
  animation: typing-dot 1.2s ease-in-out infinite;
}

#twin-chat .typing-bubble span:nth-child(2) { animation-delay: 0.15s; }
#twin-chat .typing-bubble span:nth-child(3) { animation-delay: 0.3s; }

@keyframes typing-dot {
  0%, 60%, 100% { opacity: 0.35; transform: translateY(0); }
  30% { opacity: 1; transform: translateY(-3px); }
}

/* ----------------------------- Composer */
#composer {
  align-items: stretch !important;
  gap: 8px !important;
  margin-top: 0 !important;
  padding: 6px !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  background: var(--surface) !important;
  backdrop-filter: blur(20px) !important;
  -webkit-backdrop-filter: blur(20px) !important;
  box-shadow: var(--shadow-sm) !important;
}

#msg-box {
  border: 0 !important;
  background: transparent !important;
}

#msg-box textarea,
#msg-box input,
textarea,
input[type="text"] {
  min-height: 46px !important;
  padding: 12px 14px !important;
  border: 0 !important;
  border-radius: 8px !important;
  outline: none !important;
  background: var(--surface-2) !important;
  color: var(--text) !important;
  box-shadow: none !important;
  font-size: 14px !important;
  line-height: 1.45 !important;
}

#msg-box textarea:focus,
#msg-box input:focus {
  box-shadow: inset 0 0 0 2px rgba(29, 78, 216, 0.25) !important;
}

#msg-box textarea::placeholder,
#msg-box input::placeholder {
  color: var(--muted) !important;
}

/* ----------------------------- Prompts */
#prompts-section {
  transition: opacity 200ms ease, max-height 260ms ease, margin 260ms ease;
}

body.chat-active #prompts-section {
  opacity: 0;
  max-height: 0;
  margin: 0 !important;
  overflow: hidden;
  pointer-events: none;
}

.prompts-label {
  margin: 10px 0 6px;
  color: var(--muted);
  font-size: 12px;
  font-weight: 600;
}

#prompt-grid {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  gap: 8px !important;
}

button.prompt-card {
  width: 100% !important;
  min-height: 52px !important;
  padding: 10px 12px !important;
  justify-content: flex-start !important;
  text-align: left !important;
  border-radius: 10px !important;
  border-color: var(--border) !important;
  background: var(--surface) !important;
  color: var(--muted) !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  line-height: 1.35 !important;
}

button.prompt-card:hover {
  border-color: var(--accent) !important;
  background: var(--accent-soft) !important;
  color: var(--text) !important;
}

/* ----------------------------- Info panels (About / Resume / Projects) */
.info-panel {
  padding: 4px 2px 8px;
}

.info-panel h2 {
  margin: 0 0 8px;
  font-size: 20px;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--text);
}

.info-panel .lead {
  margin: 0 0 18px;
  max-width: 62ch;
  color: var(--muted);
  font-size: 14px;
  line-height: 1.65;
}

.info-panel strong {
  color: var(--text) !important;
  font-weight: 700;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
  margin-bottom: 16px;
}

.info-card {
  padding: 14px 16px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--surface);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.info-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  border-color: var(--accent);
}

.info-card h3,
.info-card strong {
  margin: 0 0 8px;
  font-size: 13px;
  font-weight: 700;
  color: var(--text) !important;
}

.info-card p,
.info-card li {
  margin: 0 0 6px;
  color: var(--muted);
  font-size: 13px;
  line-height: 1.55;
}

.info-card ul {
  margin: 0;
  padding-left: 1.1rem;
}

.info-card li:last-child,
.info-card p:last-child {
  margin-bottom: 0;
}

.info-cta {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.info-cta a {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  padding: 0 14px;
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--accent);
  background: var(--accent-soft);
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
}

.info-cta a:hover {
  border-color: var(--accent);
  background: #dbeafe;
}

.panel-note {
  margin: 16px 0 12px;
  color: var(--muted);
  font-size: 13px;
  line-height: 1.55;
}

.project-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.project-card {
  padding: 14px 16px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--surface);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.project-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  border-color: var(--accent);
}

.project-card h3 {
  margin: 0 0 6px;
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
}

.project-card p {
  margin: 0 0 10px;
  color: var(--muted);
  font-size: 13px;
  line-height: 1.5;
}

.tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 10px;
}

.tag-row span {
  padding: 3px 8px;
  border-radius: 999px;
  background: var(--surface-2);
  color: var(--muted);
  font-size: 11px;
  font-weight: 600;
}

.project-link {
  color: var(--accent) !important;
  font-size: 12px;
  font-weight: 600;
  text-decoration: none;
}

.project-link:hover {
  text-decoration: underline;
}

/* ----------------------------- Scrollbar & selection */
::selection {
  background: #bfdbfe;
  color: var(--text);
}

::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  border-radius: 999px;
  background: var(--border-strong);
}

/* ----------------------------- Responsive */
@media (max-width: 720px) {
  .gradio-container {
    padding: 12px 10px 20px !important;
  }

  .header-main {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
    padding: 12px 14px;
  }

  .header-actions {
    width: 100%;
  }

  .header-link {
    flex: 1;
    justify-content: center;
  }

  body.chat-active .header-main {
    flex-direction: row;
    align-items: center;
  }

  body.chat-active .header-actions {
    width: auto;
  }

  .main-tabs > .tab-nav,
  .main-tabs .tab-nav,
  .main-tabs [role="tablist"] {
    overflow-x: auto;
    flex-wrap: nowrap !important;
    -webkit-overflow-scrolling: touch;
  }

  #twin-chat,
  #twin-chat.chatbot,
  #twin-chat.chatbot.block {
    height: calc(100dvh - 290px) !important;
    min-height: 260px !important;
  }

  body.chat-active #twin-chat,
  body.chat-active #twin-chat.chatbot,
  body.chat-active #twin-chat.chatbot.block {
    height: calc(100dvh - 240px) !important;
  }

  #twin-chat .message-row {
    padding-left: 10px !important;
    padding-right: 10px !important;
  }

  #twin-chat .message-row :is(.message, .message-bubble, .bubble):not(:has(:is(.message, .message-bubble, .bubble))) {
    max-width: 94% !important;
  }

  #prompt-grid,
  .info-grid,
  .project-grid {
    grid-template-columns: 1fr !important;
  }

  #chat-toolbar {
    flex-wrap: wrap;
  }
}

@media (max-width: 480px) {
  #send-btn {
    min-width: 68px !important;
    padding: 0 12px !important;
  }

  .brand-text h1 {
    font-size: 16px !important;
  }
}

@media (prefers-reduced-motion: reduce) {
  #twin-chat .message-row,
  #twin-chat .typing-row,
  .chat-status[data-state="thinking"] .status-dot,
  #twin-chat .typing-bubble span {
    animation: none !important;
  }

  .site-header,
  .header-main,
  .avatar,
  .brand-subtitle,
  #prompts-section {
    transition: none !important;
  }
}
"""

JS = r"""
() => {
  document.title = "Rosheeta Sheth — Career Twin";

  const body = document.body;
  const chatRoot = () => document.querySelector('#twin-chat');

  const focusInput = () => {
    const input = document.querySelector('#msg-box textarea') ||
                  document.querySelector('#msg-box input');
    if (input && !input.disabled && !input.readOnly) input.focus();
  };

  const getChatScrollContainer = () => {
    const root = chatRoot();
    if (!root) return null;
    return root.querySelector('.wrapper') ||
           root.querySelector('[data-testid="chatbot"]') ||
           root.querySelector('.bubble-wrap') ||
           root;
  };

  const scrollChatToBottom = () => {
    const container = getChatScrollContainer();
    if (!container) return;
    container.scrollTop = container.scrollHeight;
  };

  const hasUserMessage = () => {
    const root = chatRoot();
    if (!root) return false;
    return Boolean(
      root.querySelector('.user-row') ||
      root.querySelector('[data-role="user"]')
    );
  };

  const syncConversationState = () => {
    body.classList.toggle('chat-active', hasUserMessage());
  };

  const removeTypingIndicator = () => {
    document.querySelectorAll('#twin-chat .typing-row').forEach((node) => node.remove());
  };

  const showTypingIndicator = () => {
    const root = chatRoot();
    if (!root || root.querySelector('.typing-row')) return;

    const row = document.createElement('div');
    row.className = 'message-row bot-row typing-row';
    row.setAttribute('aria-label', 'Assistant is typing');
    row.innerHTML = '<div class="typing-bubble"><span></span><span></span><span></span></div>';

    const container = getChatScrollContainer();
    if (container) {
      container.appendChild(row);
      scrollChatToBottom();
    }
  };

  const syncTypingFromStatus = () => {
    const status = document.querySelector('.chat-status');
    if (!status) return;
    if (status.dataset.state === 'thinking') {
      showTypingIndicator();
    } else {
      removeTypingIndicator();
    }
  };

  const watchStatus = () => {
    const statusWrap = document.querySelector('#status-wrap');
    if (!statusWrap || statusWrap.dataset.careerTwinWatched) return;
    statusWrap.dataset.careerTwinWatched = 'true';

    const observer = new MutationObserver(() => {
      syncTypingFromStatus();
    });

    observer.observe(statusWrap, { childList: true, subtree: true, characterData: true });
    syncTypingFromStatus();
  };

  const watchChat = () => {
    const root = chatRoot();
    if (!root || root.dataset.careerTwinWatched) return;
    root.dataset.careerTwinWatched = 'true';

    const observer = new MutationObserver(() => {
      syncConversationState();
      scrollChatToBottom();
    });

    observer.observe(root, { childList: true, subtree: true });
    syncConversationState();
  };

  const watchInput = (input) => {
    if (!input || input.dataset.careerTwinWatched) return;
    input.dataset.careerTwinWatched = 'true';
    let wasDisabled = input.disabled || input.readOnly;
    new MutationObserver(() => {
      const disabled = input.disabled || input.readOnly;
      if (wasDisabled && !disabled) focusInput();
      wasDisabled = disabled;
    }).observe(input, {
      attributes: true,
      attributeFilter: ['disabled', 'readonly']
    });
  };

  const scan = () => {
    watchChat();
    watchStatus();
    watchInput(document.querySelector('#msg-box textarea'));
    watchInput(document.querySelector('#msg-box input'));
  };

  setTimeout(focusInput, 350);
  setTimeout(scan, 400);
  setTimeout(scan, 1200);

  new MutationObserver(scan).observe(document.body, {
    childList: true,
    subtree: true
  });

  document.addEventListener('keydown', (event) => {
    const active = document.activeElement;
    const typing = active && ['INPUT', 'TEXTAREA'].includes(active.tagName);
    if (event.key === '/' && !typing) {
      event.preventDefault();
      focusInput();
    }
  });
}
"""

__all__ = ["CSS", "JS", "EXAMPLES", "HEADER_HTML"]
