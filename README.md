# Restaurant Name Menu Recommender

An AI-powered app that suggests menu items based on the restaurant name or cuisine.  
Securely manages API keys with \`.env\` and uses virtual environments for easy setup.

---

## 🚀 Setup Instructions

1. **Clone the repository**  
   git clone https://github.com/alee-kolachi/restaurant-name-menu-recommender.git
   cd restaurant-name-menu-recommender
2. **Create & activate a virtual environment**  
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**  
   pip install -r requirements.txt

4. **Configure environment variables**  
   Create a .env file in the root folder with your API key(s):  
   API_KEY=your_api_key_here

5. **Run the app**  
   python main.py

---

## 🔒 Security

- .env and venv/ directories are included in .gitignore to keep secrets and dependencies out of version control.

---

## 📄 License

MIT License (or your preferred license)
