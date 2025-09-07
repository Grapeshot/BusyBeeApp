#!/usr/bin/env python3
"""
Database reset utility for BusyBee app
This script will wipe all data from the SQLite database
"""

import os
import sqlite3

def reset_database():
    """Reset the database by deleting and recreating it"""
    db_file = 'tasks.db'
    
    print("🗑️  Resetting BusyBee database...")
    
    # Delete the database file if it exists
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"✅ Deleted {db_file}")
    else:
        print(f"ℹ️  {db_file} doesn't exist")
    
    # Recreate the database with empty tables
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Create the tasks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            done BOOLEAN DEFAULT FALSE
        )
    ''')
    
    conn.commit()
    conn.close()
    
    print("✅ Database reset complete!")
    print("📋 Fresh tasks table created")
    print("🚀 Ready for new data")

def clear_tasks_only():
    """Clear all tasks but keep the database structure"""
    db_file = 'tasks.db'
    
    if not os.path.exists(db_file):
        print("❌ Database doesn't exist. Run reset_database() first.")
        return
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Count tasks before deletion
    cursor.execute('SELECT COUNT(*) FROM tasks')
    count = cursor.fetchone()[0]
    
    # Delete all tasks
    cursor.execute('DELETE FROM tasks')
    
    conn.commit()
    conn.close()
    
    print(f"🗑️  Deleted {count} tasks")
    print("✅ Database cleared (structure preserved)")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--clear-only':
        clear_tasks_only()
    else:
        reset_database()
