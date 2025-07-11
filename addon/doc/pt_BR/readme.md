# Event Tracker #

* Autores: Joseph Lee, Thiago Seus

Esse complemento gera informações sobre objetos para os quais os eventos
foram disparados. As propriedades registradas no modo de log de depuração
incluem tipo de objeto, nome, função, evento, módulo de aplicativo e
informações específicas da API de acessibilidade, como accName para objetos
IAccessible e Automation Id para objetos UIA.

Notas:

* Esse complemento foi projetado para desenvolvedores e usuários avançados
  que precisam rastrear eventos provenientes de aplicativos e vários
  controles.
* Para usar o complemento, o NVDA deve estar registrando em modo de
  depuração (configurado nas configurações gerais/nível de registro ou
  reiniciar com o registro de depuração ativado).
* Pode ser possível que os complementos carregados antes do Event Tracker
  não transmitam o evento para outros complementos, inclusive o Event
  Tracker. Se isso acontecer, o Event Tracker não conseguirá registrar os
  eventos.
* Os eventos são tratados a partir de plug-ins globais, módulos de
  aplicativos, interceptores de árvore e objetos NVDA, nessa ordem.

## Eventos e suas informações

Os seguintes eventos são rastreados e registrados:

* Manipulação de foco: ganhar foco, perder o foco, foco inserido, primeiro
  plano
* Alterações: nome, valor, estado, descrição, região ativa
* Outros eventos: alerta
* Eventos UIA: controlador para, efeitos de destino de arrastar e soltar,
  elemento selecionado, status do item, layout invalidado, notificação,
  alerta do sistema, alteração de texto, dica de ferramenta aberta, janela
  aberta

Para cada evento, as seguintes informações serão registradas:

* Nome do evento
* Objeto
* Nome do objeto
* Função do objeto
* Valor ou estado do objeto dependendo dos eventos
* Módulo de aplicativo
* Para objetos IAccessible: nome da conta, ID do filho
* Para objetos UIA: Id de automação, nome da classe, propriedades de
  notificação se estiver registrando informações de evento de notificação,
  contagem de filhos para evento de invalidação de layout, propriedades para
  status de item, arrastar e soltar e efeito de destino, se definido

Também é possível atribuir um gesto para visualizar os eventos em uma lista
(menu NVDA/Preferências/Gestos de entrada, categoria Event Tracker). A lista
salva até 100 eventos mais recentes processados.

If you find this add-on useful, please [review it][1] in the NVDA Add-on
Store.

## Version 25.1.0

* NVDA 2025.1 compatibility.
* NVDA 2024.1 or later is required due to Python 3.11 upgrade.
* Restored limited support for Windows 8.1.
* Made the add-on code more robust with help from Pyright (a Python static
  type checker).
* NVDA will record actual control role name instead of integers when
  reporting events.

## Versão 24.1.0

* Compatibilidade com o NVDA 2024.1.
* opensourcesys/evtTracker #4: the first event's description no longer
  missing when first opening the event viewer. Contributed by: WangFeng
  Huang (hwf1324)

## Versão 23.02

* É necessário o NVDA 2022.4 ou posterior.
* É necessário o Windows 10 21H2 (atualização/compilação 19044 de novembro
  de 2021) ou posterior.
* O evento de alerta (principalmente para objetos IAccessible) será
  rastreado.

## Versão 23.01

* É necessário o NVDA 2022.3 ou posterior.
* É necessário ter o Windows 10 ou posterior, pois o Windows 7, 8 e 8.1 não
  serão mais suportados pela Microsoft a partir de janeiro de 2023.

## Versão 22.12

* Adicionada a caixa de diálogo da lista de eventos (comando não atribuído)
  para listar até 100 eventos recentes registrados pelo complemento (Thiago
  Seus).
* Informações adicionais sobre o evento, como propriedades de notificação
  UIA, são registradas ao mesmo tempo que os eventos.

## Versão 22.10

* O NVDA 2022.2 ou posterior é necessário devido à segurança.
* As seguintes alterações de propriedade do UIA são rastreadas: efeito de
  arrastar e soltar, efeito de destino.
* O texto da propriedade de status do item UIA é registrado.
* O NVDA não reproduzirá mais tons de erro ou parecerá não fazer nada se um
  objeto não definir um nome de classe de janela.

## Versão 22.06

* O NVDA 2021.3 ou posterior é necessário devido à segurança.

## Versão 21.10

* O NVDA 2021.2 ou posterior é necessário devido a alterações no NVDA que
  afetam esse complemento.
* O evento invalidado do layout UIA será rastreado.
* As informações de função e estados do objeto serão semelhantes às
  informações do desenvolvedor encontradas em versões mais recentes do NVDA.

## Versão 21.07

* Lançamento inicial.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
