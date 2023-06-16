# Rastreador de eventos #

* Autor: Joseph Lee, Thiago Seus, Luke Davis
* Descargar [versión estable][1]
* Compatibilidad con NVDA: de 2022.4 en adelante

Este complemento emite información sobre objetos en los que se han disparado
eventos. Entre las propiedades registradas en el nivel de registro de
depuración se incluyen el tipo de objeto, su nombre, rol, evento, módulo de
aplicación, e información específica de la API de accesibilidad como el
accName del objeto IAccessible y el Id de automatización en objetos UIA.

Notas:

* Este complemento está pensado para desarrolladores y usuarios avanzados
  que necesitan rastrear eventos procedentes de aplicaciones y diversos
  controles.
* Para usar el complemento, NVDA debe tener el registro en modo depuración
  (configurado desde Opciones generales / Nivel de registro, o reiniciado
  con el registro de depuración habilitado).
* Podría ser posible que los complementos cargados antes que el reastreador
  de eventos no pasen el evento a otros complementos, incluido el rastreador
  de eventos. Si esto sucede, el rastreador de eventos no será capaz de
  registrar eventos.
* Los eventos se manejan desde las extensiones globales, módulos de
  aplicación, interceptores de árbol y objetos de NVDA, en ese orden.

## Eventos y su información

Se rastrean y registran los siguientes eventos:

* Manipulación del foco: obtención de foco, pérdida de foco, foco
  introducido, primer plano
* Cambios: nombre, valor, estado, descripción, región viva
* Otros eventos: alerta
* Eventos UIA: controlador para, efectos de arrastrar y soltar y soltar en
  destino, elemento seleccionado, estado del elemento, diseño invalidado,
  notificación, alerta del sistema, cambio de texto, globo de ayuda abierto,
  ventana abierta

Se registra la siguiente información de cada evento:

* Nombre del evento
* Objeto
* Nombre del objeto
* Rol del objeto
* Estado o valor del objeto, dependiendo de los eventos
* Módulo de aplicación
* En objetos IAccessible: nombre acc, ID del hijo
* En objetos UIA: Id de automatización, nombre de clase, propiedades de
  notificación si se registra información de eventos de notificación,
  cantidad de hijos para el evento de diseño invalidado, propiedades de
  estado del elemento, arrastrar y soltar, y efecto de soltar en destino si
  se ha definido

También se puede asignar un gesto para visualizar los eventos en una lista
(menú NVDA / Preferencias / Gestos de entrada, categoría Rastreador de
eventos). La lista guarda hasta los 100 últimos eventos procesados.

## Versión 23.02

* Se requiere NVDA 2022.4 o posterior.
* Se requiere Windows 10 21H2 (actualización de noviembre de 2021 /
  compilación 19044) o posterior.
* Se seguirá el evento de alerta (mayoritariamente para objetos
  IAccessible).

## Versión 23.01

* Se requiere NVDA 2022.3 o posterior.
* Se requiere Windows 10 o posterior, ya que Windows 7, 8 y 8.1 ya no
  reciben soporte de Microsoft a partir de enero de 2023.

## Versión 22.12

* Añadido un diálogo de lista de eventos (orden sin asignar) para listar
  hasta los 100 eventos más recientes registrados por el complemento (Thiago
  Seus).
* La información adicional sobre el evento, como las propiedades de
  notificación UIA, se registra al mismo tiempo que el evento.

## Versión 22.10

* Se requiere NVDA 2022.2 o posterior por motivos de seguridad.
* Se rastrean los siguientes cambios de propiedades UIA: drag drop effect,
  drop target effect.
* Se registra el texto de la propiedad de estado del elemento UIA.
* NVDA ya no reproducirá tonos de error o parecerá hacer nada si un objeto
  no define un nombre de clase de ventana.

## Versión 22.06

* Se requiere NVDA 2021.3 o posterior por motivos de seguridad.

## Versión 21.10

* Se requiere NVDA 2021.2 o posterior a causa de cambios en NVDA que afectan
  a este complemento.
* Se seguirá el evento UIA diseño invalidado.
* La información de rol y estados de un objeto se parecerá a la información
  para desarrolladores que se encuentra en las versiones más recientes de
  NVDA.

## Versión 21.07

* Versión inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=evtTracker
