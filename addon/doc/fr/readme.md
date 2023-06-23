# Event Tracker #

* Auteur : Joseph Lee, Thiago Seus, Luke Davis
* Télécharger [version stable][1]
* Compatibility NVDA : 2022.4 et supérieure

Cette extension affiche des informations sur les objets pour lesquels des
événements ont été déclenchés. Les propriétés enregistrées dans le mode de
log de débugage comprennent le type d'objet, le nom, le rôle, l'événement,
le module applicatif et des informations spécifiques à l'API d'accessibilité
telles que accName pour l'objet IAccessible et Automation Id pour les objets
UIA.

Notes :

* Cette extension est conçue pour les développeurs et les utilisateurs
  expérimentés qui ont besoin de suivre des événements provenant d'applis et
  divers contrôles.
* Pour utiliser l'extension, NVDA doit se connecter en mode débogage
  (configuré à partir des paramètres généraux/niveau de journalisation, ou
  redémarrer avec le journal activé en mode débogage).
* Il est possible que les extensions chargées avant Event Tracker ne
  communiquent pas l'événement à d'autres extensions, y compris Event
  Tracker. Si c'est le cas, Event Tracker ne sera pas en mesure
  d'enregistrer les événements.
* Les événements sont gérés dans l'ordre par les modules globaux, modules
  applicatifs, les intercepteurs d'arborescence et les objets NVDA.

## Les événements et leurs informations

Les événements suivants sont suivis et enregistrés :

* La manipulation du focus : réception du focus, perte du focus, le focus
  obtenu, le premier plan
* Les changements : nom, valeur, état, description, live region
* Autres événements : alerte
* Les événements UIA : le contrôleur, les effets glisser-déposer et déposer
  sur la sible, l'élément sélectionné, le statut de l'élément, la
  présentation invalidé, la notification, l'alerte système, la modification
  du texte, l'ouverture d'une bule d'aide, l'ouverture d'une fenêtre

Pour chaque événement, les informations suivantes sont enregistrées :

* Le nom de l'événement
* L'objet
* Le nom de l'objet
* Le rôle de l'objet
* La valeur ou l'état de l'objet en fonction des événements
* Module d'app
* Pour les objets IAccessible : acc name, child ID
* Pour les objets UIA : Automation Id, le nom de la classe, les propriétés
  de la notification si enregistrement de la notification de l'information
  de l'événement, le nombre d'enfants de l'événement pour la présentation
  invalidé, les propriétés pour le statut de l'élément, le glisser/déposer
  et l'effet de déposer sur la sible s'il est défini

Vous pouvez également assigner un geste pour afficher les événements d'une
liste (menu NVDA / Préférences / Gestes de commandes, catégorie  Event
Tracker). la liste sauvegarde jusqu'à 100 derniers événements traités.

## Version 23.02

* NVDA 2022.4 ou version ultérieure est requis.
* Windows 10 21H2 (November 2021 Update/build 19044) ou ultérieure est
  requise.
* L'événement d'alerte (principalement pour les objets IAccessible) sera
  suivi.

## Version 23.01

* NVDA 2022.3 ou version ultérieure est requis.
* Windows 10 ou ultérieure est requis car Windows 7, 8 et 8.1 ne sont plus
  pris en charge par Microsoft en janvier 2023.

## Version 22.12

* Ajout d'un dialogue de liste des événements (commande non assigné) pour
  répertorier jusqu'à 100 événements récents enregistrés par l'extension
  (Thiago Seus).
* Les informations supplémentaires sur les événements telles que les
  propriétés de la notification UIA sont enregistrées en même temps que les
  événements.

## Version 22.10

* NVDA 2022.2 ou version ultérieure est requis en raison de sécurité.
* Les changements de propriété UIA suivants sont suivis : drag drop effect,
  drop target effect.
* Le texte de la propriété de l'État de l'élément UIA est journalisé.
* NVDA ne jouera plus de tonalités d'erreur ou ne semblera rien faire si un
  objet ne définit pas le nom de la classe de fenêtre.

## Version 22.06

* NVDA 2021.3 ou version ultérieure est requis en raison de sécurité.

## Version 21.10

* NVDA 2021.2 ou version ultérieure est requis en raison de modifications de
  NVDA qui affectent cette extension.
* L'événement UIA layout invalidated sera suivi.
* Les informations sur les rôles et états d'un objet ressembleront à les
  informations Pour les développeurs trouvés dans les versions les plus
  récentes de NVDA.

## Version 21.07

* Première version.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=evtTracker
