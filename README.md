meus gatos são muito fofos

# 📩 Envio Automático de E-mail de Boas-Vindas – Workflow n8n + Supabase

Este workflow em **n8n** automatiza o envio de e-mails de boas-vindas sempre que um novo usuário é cadastrado. Ele utiliza **Supabase** como banco de dados e **SMTP** para envio dos e-mails.

---

## ⚙️ Fluxo do Workflow

### 1. 🟢 Disparo Manual
- **Trigger**: `Manual Trigger`
- Usado para testes no n8n. No ambiente de produção, deve ser substituído por um Webhook (ex: do cadastro real).

---

### 2. 📝 Criação do Usuário no Supabase
- **Node:** `Create a row`
- **Tabela:** `usuarios`
- Cadastra os dados do novo usuário:
  - `nome`: fornecido ou `"usuário temporário"`
  - `email`: fornecido ou `"isaqueteste@teste.com"`
  - `senha`: fornecida ou `"123456"`

---

### 3. 🧠 Geração de Conteúdo do E-mail
- **Node:** `Code`
- Cria:
  - Assunto personalizado (`Seja bem-vindo à Crescitec, {nome}`)
  - Corpo do e-mail com mensagem motivacional

---

### 4. 📧 Envio do E-mail
- **Node:** `Send email`
- Envia o e-mail usando uma conta SMTP:
  - **Remetente:** `isaquecarvalho2007@gmail.com`
  - **Destinatário:** o e-mail fornecido no cadastro
  - **Formato:** Texto puro (`text/plain`)

---

### 5. 📊 Registro no Log de E-mails
- **Node:** `Create a row1`
- **Tabela:** `log_email`
- Campos registrados:
  - `tipo`: `"boas_vindas"`
  - `status`: `"enviado"`
  - `criado_em`: timestamp ISO da data/hora

---

## 🧾 Estrutura Esperada no Supabase

### 📂 Tabela: `usuarios`
| Campo   | Tipo   | Descrição                  |
|---------|--------|----------------------------|
| nome    | text   | Nome do usuário            |
| email   | text   | E-mail do usuário          |
| senha   | text   | Senha definida no cadastro |

### 📂 Tabela: `log_email`
| Campo      | Tipo   | Descrição                    |
|------------|--------|------------------------------|
| tipo       | text   | Tipo de e-mail enviado        |
| status     | text   | Status do envio               |
| criado_em  | text   | Data/hora ISO (timestamp UTC) |

---

## ✅ Benefícios do Workflow

- Automação completa do envio de boas-vindas
- Registro em banco para rastreabilidade
- Pronto para substituir por Webhook em produção
- Pode ser integrado com API externa, WebApp, WhatsApp, etc.

---

## 📦 Possíveis Melhorias Futuras

- Adicionar validação do e-mail
- Lógica de reenvio em caso de erro
- Substituir trigger manual por Webhook (ex: formulário de cadastro)
- Customização da mensagem por categoria de usuário

---

> Desenvolvido com 💙 usando [n8n](https://n8n.io), Supabase e SMTP
