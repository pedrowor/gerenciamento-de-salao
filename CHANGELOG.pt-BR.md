# Histórico de alterações

Este arquivo registra pequenas alterações de manutenção do projeto. Alterações não publicadas são revisadas em pull requests antes de serem incorporadas.

## Não publicado

### Corrigido
- Listagens e relatórios de agendamentos agora exibem um traço quando o valor do serviço não está registrado, sem causar erro de formatação.
- Ao editar um agendamento sem valor registrado no banco, o campo de preço permanece vazio.

### Testes
- Adicionados testes de regressão focados em valores ausentes e preços numéricos normais, sem necessidade de interface gráfica.
