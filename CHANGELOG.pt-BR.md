# Histórico de alterações

Este arquivo registra pequenas alterações de manutenção do projeto. Alterações não publicadas são revisadas em pull requests antes de serem incorporadas.

## Não publicado

### Adicionado
- Cadastro de contas e entrada com senha para usuários locais.
- Armazenamento de senhas com salt individual e PBKDF2-HMAC-SHA256.
- Atualização da tabela de usuários sem apagar os agendamentos existentes.

### Alterado
- Removido o acesso padrão somente pelo nome de usuário. Contas antigas sem hash de senha não podem entrar; é necessário cadastrar uma nova conta.

### Testes
- Adicionados testes de cadastro, autenticação, usuário duplicado e migração do banco de dados.

### Corrigido
- Listagens e relatórios de agendamentos agora exibem um traço quando o valor do serviço não está registrado, sem causar erro de formatação.
- Ao editar um agendamento sem valor registrado no banco, o campo de preço permanece vazio.

### Testes
- Adicionados testes de regressão focados em valores ausentes e preços numéricos normais, sem necessidade de interface gráfica.
