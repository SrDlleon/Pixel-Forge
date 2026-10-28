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

---

## 28/10/2026

**O que foi feito:**
- Criação e organização dos templates HTML.
- Desenvolvimento das páginas de clientes, jogos e desenvolvedoras.
- Criação dos formulários de cadastro, edição e exclusão.
- Desenvolvimento do controller de jogos com as funcionalidades de cadastro, listagem, detalhes, edição e exclusão.
- Integração das rotas de jogos com os templates e o banco de dados.
- Correção de erros nas rotas, formulários e associação dos jogos às desenvolvedoras.
- Realização de testes para verificar o funcionamento das funcionalidades de jogos.

**Dificuldade encontrada:**
- Organizar os templates de forma simples.
- Corrigir problemas na integração entre as rotas, os formulários e o banco de dados.

**Como resolvi:**
- Organizei os templates com suas funcionalidades principais.
- Corrigi as rotas e consultas utilizando Flask e SQLAlchemy.
- Mantive o código simples e realizei testes para verificar as correções.

**Próximo passo:**
- Integrar o controller de jogos aos controllers de clientes e desenvolvedoras quando estiverem prontos.
- Testar o funcionamento completo da aplicação.