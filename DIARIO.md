# Diário de Desenvolvimento — Pixel Forge

## 20/10/2026

**O que foi feito:**
- Configuração do banco de dados SQLite com SQLAlchemy.
- Criação dos modelos Cliente, Jogo e Desenvolvedora.
- Implementação dos relacionamentos 1:N e N:N.
- Criação da tabela intermediária `cliente_jogo`.
- Implementação do arquivo `seed.py` para popular o banco com dados iniciais.
- Apresentação do sistema e dos integrantes no README, por Larícia.

**Dificuldade encontrada:**
- Entender como implementar os relacionamentos utilizando a sintaxe moderna do SQLAlchemy 2.x.

**Como resolvi:**
- Utilizei `Mapped`, `mapped_column`, `relationship` e `ForeignKey` para definir os modelos e seus relacionamentos.

**Próximo passo:**
- Criar os templates HTML e começar a desenvolver os Controllers para realizar as operações de cadastro, listagem, edição e exclusão.

---

## 28/10/2026

**O que foi feito:**
- Criação e organização dos templates HTML, por Larícia.
- Desenvolvimento das páginas de clientes, jogos e desenvolvedoras.
- Criação dos formulários de cadastro, edição e exclusão.
- Desenvolvimento do controller de jogos com as funcionalidades de cadastro, listagem, detalhes, edição e exclusão, por Davi (SrDlleon no Git).
- Integração das rotas de jogos com os templates e o banco de dados.
- Listagem dos clientes associados a um jogo.
- Correção de erros nas rotas, formulários e associação dos jogos às desenvolvedoras.
- Realização de testes para verificar o funcionamento das funcionalidades de jogos.
- Descrição das entidades e dos relacionamentos no README, por Larícia.
- Início da estrutura do controller de desenvolvedoras, por Larícia.

**Dificuldade encontrada:**
- Organizar os templates de forma simples.
- Corrigir problemas na integração entre as rotas, os formulários e o banco de dados.

**Como resolvi:**
- Organizei os templates com suas funcionalidades principais.
- Corrigi as rotas e consultas utilizando Flask e SQLAlchemy.
- Mantive o código simples e realizei testes para verificar as correções.

**Próximo passo:**
- Continuar o desenvolvimento do controller de desenvolvedoras e ajustar suas rotas para funcionar com os templates.

---

## 29/10/2026

**O que foi feito:**
- Organização do controller de desenvolvedoras em `controllers/desenvolvedoras/routes.py` e registro do Blueprint no `app.py`, por Larícia.
- Início da consulta para listar desenvolvedoras, ainda com ajustes pendentes.
- Uso do template da página inicial e correção do link "Ver jogos".

**Dificuldade encontrada:**
- Organizar as rotas do Blueprint e fazer a listagem buscar os dados corretos do banco.

**Como resolvi:**
- As rotas foram reunidas na pasta de desenvolvedoras e o import do Model foi corrigido.
- A página inicial passou a usar `index.html` e o link passou a apontar para a rota de listagem de jogos.
- A consulta de desenvolvedoras ficou para ser ajustada na próxima etapa.

**Próximo passo:**
- Corrigir a listagem de desenvolvedoras e implementar as funcionalidades de cadastro, edição e exclusão.

---

## 30/10/2026

**O que foi feito:**
- Cadastro, listagem, detalhes, edição e exclusão de desenvolvedoras, por Larícia.
- Integração do CRUD com os templates de desenvolvedoras.
- Inclusão da verificação de jogos vinculados antes de excluir uma desenvolvedora.

**Dificuldade encontrada:**
- A listagem anterior consultava `Jogo` e enviava uma variável diferente da esperada pelo template.
- Garantir que uma desenvolvedora com jogos cadastrados não fosse excluída.

**Como resolvi:**
- A consulta foi ajustada para buscar desenvolvedoras e enviar a lista esperada pelo template.
- A rota de listagem foi ajustada para usar o prefixo já definido no Blueprint.
- Foi adicionada uma verificação dos jogos vinculados antes da exclusão.

**Próximo passo:**
- Desenvolver o controller de clientes e implementar a biblioteca para adicionar e remover jogos.

---

## 31/10/2026

**O que foi feito:**
- Cadastro, listagem, perfil, edição e exclusão de clientes, por Aislanny.
- Uso de hash nas senhas e manutenção da senha atual quando o campo de edição fica vazio.
- Biblioteca dos clientes com adição e remoção de jogos.
- Registro do Blueprint de clientes no `app.py` e integração das alterações do grupo, por Aislanny.
- Atualização do README com as responsabilidades dos integrantes, as instruções de execução e as dificuldades do projeto, por Larícia.

**Dificuldade encontrada:**
- O cadastro inicial tinha um nome incorreto no redirecionamento e usava `none` no lugar de `None`.
- Integrar a biblioteca dos clientes com os jogos cadastrados no banco.

**Como resolvi:**
- O cadastro passou a usar a rota `/novo`, o redirecionamento para `clientes.listar` e o valor `None` no formulário.
- As rotas de perfil, biblioteca, edição e exclusão foram ligadas aos templates e às operações do banco.
- A biblioteca passou a utilizar o relacionamento entre clientes e jogos para adicionar e remover os registros.

**Próximo passo:**
- Testar a aplicação completa, verificar a integração entre os Controllers e corrigir possíveis erros antes da entrega final.