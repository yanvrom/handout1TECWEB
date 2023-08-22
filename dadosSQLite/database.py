import sqlite3
from dataclasses import dataclass

class Database:
    def __init__(self, nome):
        self.conn = sqlite3.connect(nome + '.db')
        self.cur = self.conn.cursor()
        comando = """
            CREATE TABLE IF NOT EXISTS note (
                id INTEGER PRIMARY KEY,
                title TEXT,
                content TEXT NOT NULL
            );
        """
        self.cur.execute(comando)
    
    def add(self, note):
        comando = f"""
            INSERT INTO note (id, title, content) VALUES
                (
                    
                );
        """
        
@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''