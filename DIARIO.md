# Diário de Desenvolvimento — Pixel Forge

## 20/10/2026

**O que foi feito:**
- Configuração do banco de dados SQLite com SQLAlchemy.
- Criação dos modelos Cliente, Jogo e Desenvolvedora.
- Implementação dos relacionamentos 1:N e N:N.
- Criação da tabela intermediária `cliente_jogo`.
- Implementação do arquivo `seed.py` para popular o banco com dados iniciais.

**Dificuldade encontrada:**
- Entender como implementar os relacionamentos utilizando a sintaxe moderna do SQLAlchemy 2.x.

**Como resolvi:**
- Utilizei `Mapped`, `mapped_column`, `relationship` e `ForeignKey` para definir os modelos e seus relacionamentos.

**Próximo passo:**
- Desenvolver os Controllers e implementar as funcionalidades básicas de cadastro, listagem, edição e exclusão (CRUD).

 **Data:** 28/10/2026

**O que foi feito:**
- Criação e organização dos templates HTML.
- Desenvolvimento das páginas de clientes, jogos e desenvolvedoras.
- Criação dos formulários de cadastro, edição e exclusão.

**Dificuldade encontrada:**
- Organizar os templates de forma simples.

**Como resolvi:**
- Organizei os templates com suas funcionalidades principais.

**Próximo passo:**
- Integrar os templates aos Controllers e testar o funcionamento das páginas.
  
