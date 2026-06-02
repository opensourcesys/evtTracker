# Rastreador de eventos

* Autores: Joseph Lee, Thiago Seus

Este complemento emite información sobre objetos en los que se han disparado eventos. Entre las propiedades registradas en el nivel de registro de depuración se incluyen el tipo de objeto, su nombre, rol, evento, módulo de aplicación, e información específica de la API de accesibilidad como el accName del objeto IAccessible y el Id de automatización en objetos UIA.

Notas:

* Este complemento está pensado para desarrolladores y usuarios avanzados que necesitan rastrear eventos procedentes de aplicaciones y diversos controles.
* Para usar el complemento, NVDA debe tener el registro en modo depuración (configurado desde Opciones generales / Nivel de registro, o reiniciado con el registro de depuración habilitado).
* Podría ser posible que los complementos cargados antes que el reastreador de eventos no pasen el evento a otros complementos, incluido el rastreador de eventos. Si esto sucede, el rastreador de eventos no será capaz de registrar eventos.
* Los eventos se manejan desde las extensiones globales, módulos de aplicación, interceptores de árbol y objetos de NVDA, en ese orden.

## Eventos y su información

Se rastrean y registran los siguientes eventos:

* Manipulación del foco: obtención de foco, pérdida de foco, foco introducido, primer plano
* Cambios: nombre, valor, estado, descripción, región viva
* Otros eventos: alerta
* Eventos UIA: controlador para, efectos de arrastrar y soltar y soltar en destino, elemento seleccionado, estado del elemento, diseño invalidado, notificación, alerta del sistema, cambio de texto, globo de ayuda abierto, ventana abierta

Se registra la siguiente información de cada evento:

* Nombre del evento
* Objeto
* Nombre del objeto
* Rol del objeto
* Estado o valor del objeto, dependiendo de los eventos
* Módulo de aplicación
* En objetos IAccessible: nombre acc, ID del hijo
* En objetos UIA: Id de automatización, nombre de clase, propiedades de notificación si se registra información de eventos de notificación, cantidad de hijos para el evento de diseño invalidado, propiedades de estado del elemento, arrastrar y soltar, y efecto de soltar en destino si se ha definido

También se puede asignar un gesto para visualizar los eventos en una lista (menú NVDA / Preferencias / Gestos de entrada, categoría Rastreador de eventos). La lista guarda hasta los 100 últimos eventos procesados.

Si encuentras útil este complemento, [reséñalo][1] en la tienda de complementos de NVDA.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
