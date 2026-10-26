import sqlite3
from sqlite3 import Error

DATABASE_NAME = "database.db"

def connect_db():
    """Cria uma conexão com o banco de dados SQLite."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        # print(f"Conexão bem-sucedida com {DATABASE_NAME}")
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conn

def create_table(conn, create_table_sql):
    """Cria uma tabela a partir da instrução SQL fornecida."""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(f"Erro ao criar tabela: {e}")

def setup_database():
    """
    Configura o banco de dados: cria a conexão e as tabelas necessárias
    (agendamentos e usuarios) caso elas não existirem.
    """
    
    # SQL para criar a tabela de agendamentos (clientes agendados)
    sql_create_agendamentos_table = """
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        email TEXT,
        data TEXT NOT NULL,          -- Formato sugerido: 'YYYY-MM-DD HH:MM'
        valor_servico REAL,          -- Usar REAL para valores monetários
        servico TEXT NOT NULL
    );
    """

    # Armazena somente hash de senha; usuários antigos terão NULL até migrarem.
    sql_create_usuarios_table = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT
    );
    """

    # Cria a conexão com o banco
    conn = connect_db()

    # Cria as tabelas se a conexão foi bem-sucedida
    if conn is not None:
        print("Criando/Verificando tabelas...")
        create_table(conn, sql_create_agendamentos_table)
        create_table(conn, sql_create_usuarios_table)
        
        # Atualização não destrutiva de bancos criados com login por usuário.
        try:
            existing_columns = {
                row[1] for row in conn.execute("PRAGMA table_info(usuarios)")
            }
            if "password_hash" not in existing_columns:
                conn.execute("ALTER TABLE usuarios ADD COLUMN password_hash TEXT")
            conn.commit()
        except Error as e:
            print(f"Erro ao atualizar a tabela de usuários: {e}")

        # Fecha a conexão
        conn.close()
        print("Configuração do banco de dados concluída.")
    else:
        print("Erro! Não foi possível criar uma conexão com o banco de dados.")
