from telegram.ext import ApplicationBuilder
from bot import register_handlers
from bot.config import BOT_TOKEN, FIREBASE_CONFIG
import firebase_admin
from firebase_admin import credentials

def main():
    try:
        # Initialize Firebase only if not already initialized
        if not firebase_admin._apps:
            cred = credentials.Certificate(FIREBASE_CONFIG)
            print("🔥 Initializing Firebase...")
            firebase_admin.initialize_app(cred)
            print("✅ Firebase initialized successfully.")
            
        else:
            print("✅ Firebase already initialized.")
            
        
        # Create and start the bot
        print("🤖 Starting Telegram bot...")
        app = ApplicationBuilder().token(BOT_TOKEN).build()
        register_handlers(app)
        
        # Run the bot
        app.run_polling()
        
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        # Clean up Firebase connection when bot stops
        if firebase_admin._apps:
            print("🔥 Closing Firebase connection...")
            firebase_admin.delete_app(firebase_admin.get_app())
            print("✅ Firebase connection closed.")

if __name__ == "__main__":
    main()
