# 🔗 URL Shortener

A lightweight, self-hosted URL shortener built with **Python** and **Flask**, featuring a clean HTML frontend. Designed to be simple to deploy, easy to extend, and with future expansion into a browser extension.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Roadmap](#roadmap)
- [Browser Extension (Planned)](#browser-extension-planned)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- Shorten long URLs into compact, shareable links
- Redirect users from short URLs to their original destinations
- Clean, minimal HTML homepage for quick use
- Lightweight Flask backend — no heavy frameworks required
- Self-hosted — full control over your data

---

## 🛠 Tech Stack

| Layer     | Technology        |
|-----------|-------------------|
| Backend   | Python 3, Flask   |
| Frontend  | HTML, CSS         |
| Storage   | (e.g. SQLite / in-memory — update as appropriate) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip` package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/danielwalter0/url-shortener.git
   cd url-shortener
   ```

2. **Create and activate a virtual environment** *(recommended)*

   ```bash
   python -m venv venv

   # macOS / Linux
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Running the App

```bash
flask run
```

Or, if you're using a custom entry point:

```bash
python app.py
```

The app will be available at **http://127.0.0.1:5000** by default.

---

## 💡 Usage

1. Open the homepage in your browser.
2. Paste a long URL into the input field.
3. Click **Shorten** to generate a short link.
4. Share or use the short link — it will redirect to the original URL.

---

## 📁 Project Structure

```
url-shortener/
├── app.py                  # Main Flask application
├── database.py             # Database structure 
├── requirements.txt        # Python dependencies
├── templates/
│   ├── analytics.html      # Analytics template
│   └── index.html          # Homepage template
├── .gitignore
└── README.md
```

> **Note:** Update the structure above to match your actual project layout.

---

## ⚙️ Configuration

Copy `.env.example` to `.env` and update the values as needed:

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
BASE_URL=http://127.0.0.1:5000
```

| Variable      | Description                                  |
|---------------|----------------------------------------------|
| `SECRET_KEY`  | Flask secret key for session security        |
| `BASE_URL`    | The base URL used to prefix shortened links  |
| `FLASK_ENV`   | Set to `production` when deploying live      |

---

## 🗺 Roadmap

- [x] Basic URL shortening and redirection
- [x] HTML homepage
- [ ] Custom short codes (user-defined aliases)
- [ ] Click analytics & tracking
- [ ] User accounts and link management dashboard
- [ ] REST API for programmatic access
- [ ] QR code generation for shortened URLs
- [ ] Browser extension *(see below)*
- [ ] Docker support for easy deployment

---

## 🧩 Browser Extension (Planned)

The goal is to extend this project into a **browser extension** that allows users to shorten the current tab's URL directly from their browser toolbar — no need to visit the homepage.

**Planned features:**
- One-click shortening of the active tab URL
- Copy short link to clipboard automatically
- Popup UI showing recent links
- Works with your self-hosted instance (configurable endpoint)

> Stay tuned — contributions and ideas are welcome!

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please make sure your code follows existing conventions and includes relevant comments where appropriate.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">Built with ☕ and Python</p>
