from sqlalchemy import (
    Column, ForeignKey, Integer, Numeric, String, create_engine, func, inspect, select
)
from sqlalchemy.orm import (
    declarative_base, relationship, Session
)

Base = declarative_base()

class Cliente(Base):
  __tablename__ = "cliente"

  # atributos
  id = Column(Integer, primary_key=True, autoincrement=True)
  nome = Column(String)
  cpf = Column(String(9), nullable=False, unique=True)

  endereco = relationship(
      "Conta", back_populates="cliente"
  )

  def __repr__(self):
      return (
          f"Cliente (id={self.id}, nome = {self.nome},"
          f"cpf = {self.cpf}, numero = {self.endereco}.)"
      )

class Conta(Base):
  __tablename__ = "conta"

  # atributos
  id = Column(Integer, primary_key=True, autoincrement=True)
  tipo = Column(String)
  agencia = Column(String)
  numero = Column(Integer, unique=True)
  id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)
  saldo = Column(Numeric(precision=10, scale=2)) 

  cliente = relationship(
      "Cliente", back_populates="endereco"
  )

  def __repr__(self):
      return (
          f"Conta (id={self.id}, tipo = {self.tipo}," +
          f"agencia = {self.agencia}, numero = {self.numero}.)"
      )

# Conexão com o banco de dados
engine = create_engine("sqlite://")

# Criando as classes no banco de dados
Base.metadata.create_all(engine)

# Investiga o esquema de banco de dados
# inspetor_engine = inspect(engine)
# inspetor_engine.has_table("user")

# print(inspetor_engine.has_table("user_account"))

# print(inspetor_engine.get_table_names())
# print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    luis = Cliente(
      nome = 'Luís Dias',
      cpf = '045328932',
      endereco=[Conta(agencia='0001')]
    )

    mariana = Cliente(
       nome = 'Mariana Andrade',
       cpf = '024567212',
       endereco=[Conta(agencia='0001')]
    )

    felipe = Cliente(
       nome = 'Felipe Hugo',
       cpf = '654582134',
       endereco=[Conta(agencia='0001')]
    )

session.add_all([luis, mariana, felipe])
session.commit()

stmt = select(Cliente)

connection = engine.connect()
results = connection.execute(stmt).fetchall()

for result in results:
    print(result)

stmt = select(Cliente).where(Cliente.nome.in_(['Luís Dias', 'Mariana Andrade', 'Felipe Hugo']))
print('\nRecuperando usuários a partir de condição de filtragem')
for cliente in session.scalars(stmt):
  print("\n", cliente)
