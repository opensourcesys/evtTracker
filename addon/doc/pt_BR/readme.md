# Event Tracker

* Autores: Joseph Lee, Thiago Seus

Esse complemento gera informações sobre objetos para os quais os eventos foram disparados. As propriedades registradas no modo de log de depuração incluem tipo de objeto, nome, função, evento, módulo de aplicativo e informações específicas da API de acessibilidade, como accName para objetos IAccessible e Automation Id para objetos UIA.

Notas:

* Esse complemento foi projetado para desenvolvedores e usuários avançados que precisam rastrear eventos provenientes de aplicativos e vários controles.
* Para usar o complemento, o NVDA deve estar registrando em modo de depuração (configurado nas configurações gerais/nível de registro ou reiniciar com o registro de depuração ativado).
* Pode ser possível que os complementos carregados antes do Event Tracker não transmitam o evento para outros complementos, inclusive o Event Tracker. Se isso acontecer, o Event Tracker não conseguirá registrar os eventos.
* Os eventos são tratados a partir de plug-ins globais, módulos de aplicativos, interceptores de árvore e objetos NVDA, nessa ordem.

## Eventos e suas informações

Os seguintes eventos são rastreados e registrados:

* Manipulação de foco: ganhar foco, perder o foco, foco inserido, primeiro plano
* Alterações: nome, valor, estado, descrição, região ativa
* Outros eventos: alerta
* Eventos UIA: controlador para, efeitos de destino de arrastar e soltar, elemento selecionado, status do item, layout invalidado, notificação, alerta do sistema, alteração de texto, dica de ferramenta aberta, janela aberta

Para cada evento, as seguintes informações serão registradas:

* Nome do evento
* Objeto
* Nome do objeto
* Função do objeto
* Valor ou estado do objeto dependendo dos eventos
* Módulo de aplicativo
* Para objetos IAccessible: nome da conta, ID do filho
* Para objetos UIA: Id de automação, nome da classe, propriedades de notificação se estiver registrando informações de evento de notificação, contagem de filhos para evento de invalidação de layout, propriedades para status de item, arrastar e soltar e efeito de destino, se definido

Também é possível atribuir um gesto para visualizar os eventos em uma lista (menu NVDA/Preferências/Gestos de entrada, categoria Event Tracker). A lista salva até 100 eventos mais recentes processados.

If you find this add-on useful, please [review it][1] in the NVDA Add-on Store.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
