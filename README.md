# To-Do List — Django

Aplicação web de gerenciamento de tarefas desenvolvida com Django. Projeto construído com foco em boas práticas de desenvolvimento, separação de responsabilidades e código limpo.

---

## Funcionalidades

- Cadastro e autenticação de usuários (login/logout)
- Criar, editar e remover tarefas
- Marcar tarefas como concluídas ou reabrí-las
- Prioridade por tarefa (baixa, média, alta) com indicação visual
- Data limite (deadline) com alerta para tarefas vencidas
- Filtro por status: todas, pendentes e concluídas
- Mensagens de feedback para todas as ações relevantes
- Cada usuário acessa apenas suas próprias tarefas

---

## Tecnologias

- Python 3.12
- Django 6.0
- Bootstrap 5.3
- Bootstrap Icons
- WhiteNoise (arquivos estáticos em produção)
- Gunicorn (servidor WSGI para deploy)

---

## Estrutura do projeto

```
todo_project/
├── config/                  # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/                   # App principal
│   ├── models.py            # Modelo Task com prioridade e deadline
│   ├── views.py             # Lógica de cada rota
│   ├── services.py          # Camada de serviço (regras de negócio)
│   ├── forms.py             # Formulários de tarefa e cadastro
│   ├── urls.py              # Rotas do app
│   ├── admin.py
│   ├── migrations/
│   └── templates/
│       ├── base.html
│       ├── tasks/
│       │   ├── task_list.html
│       │   └── edit_task.html
│       └── registration/
│           ├── login.html
│           └── signup.html
├── static/
│   └── css/style.css
├── requirements.txt
├── Procfile
└── manage.py
```

---

## Como rodar localmente

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd todo_project

# 2. Crie e ative o ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute as migrações
python manage.py migrate

# 5. (Opcional) Crie um superusuário para o admin
python manage.py createsuperuser

# 6. Rode o servidor
python manage.py runserver
```

Acesse em: [http://localhost:8000](http://localhost:8000)

---

## Variáveis de ambiente

| Variável | Descrição | Padrão |
|---|---|---|
| `SECRET_KEY` | Chave secreta Django | Valor inseguro de dev |
| `DEBUG` | Modo debug | `True` |
| `ALLOWED_HOSTS` | Hosts permitidos (separados por espaço) | `localhost 127.0.0.1` |

---

## Próximos passos

- [ ] Migrar banco de dados para PostgreSQL em produção
- [ ] Adicionar paginação na lista de tarefas
- [ ] Notificações por e-mail para tarefas vencidas
- [ ] API REST para integração com apps mobile
- [ ] Kanban

---

## Objetivo

Projeto desenvolvido para praticar desenvolvimento web com Django e construir portfólio profissional.
