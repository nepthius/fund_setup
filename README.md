Demo: https://drive.google.com/file/d/1qAoMz0L1vvtIWnqwOQKJ3Lf_rSQBsCb2/view?usp=sharing

# Quickstart Setup and Installation for the code!

## Downloads
- Python 3.8+

## Installation Steps
1. Clone the repository:
    ```
    git clone https://github.com/nepthius/fund_setup.git
    cd fund_setup
    ```
2. Save the necessary vars in a .env file:
    ```
    OPENAI_API_KEY
    ```
3. Create the temporary database:
   ```
   cd backend
   python init_db.py
   ```

5. Start the backend:
   ```
   uvicorn app.main:app --reload
   ```
6. Start the Frontend:
   ```
   cd frontend
   npm install
   npm run dev
   ```

8. Access the app:
   http://localhost:5173/
   (Or the localhost link run dev prompts you)
