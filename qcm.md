# BIN-R505-DFS - Programmation avancée

## Module 1 : Votre première application Android

### Présentation de Kotlin

#### 1. Quelle déclaration de variable est valide ?

- `var hello: Int? = ""`
- `String "hello" = hello`
- `val hello = "hello"` ✅
- `hello: String = "hello"`

#### 2. Pour déclarer une variable qui ne changera pas, il est préférable d'utiliser `var` plutôt que `val`.

- Vrai
- Faux ✅

#### 3. Quelles méthodes permettent de mettre à jour une variable ? 
*Choisissez autant de réponses que vous jugez nécessaires.*

- `total++` ✅
- `total - 1`
- `total--` ✅
- `total = total + 1` ✅

#### 4. En langage Kotlin, les commentaires peuvent être composés d'une seule ou de plusieurs lignes et sont ignorés par le compilateur.

- Vrai ✅
- Faux

#### 5. Quel élément n'est pas un type de données en Kotlin ?

- `String`
- `Decimal` ✅
- `Int`
- `Boolean`

#### 6. `Float` représente également une valeur décimale, mais est moins précis que `Double`.
- Vrai ✅
- Faux

#### 7. En langage Kotlin, le point d'entrée d'un programme est l'/la ___.
- instruction `println()`
- variable `val`
- fonction `main()` ✅
- instruction `return`

#### 8. Quelles affirmations concernant les valeurs renvoyées par une fonction sont vraies ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- S'il n'est pas indiqué par une fonction, le type renvoyé est `Unit`. ✅
- Une valeur renvoyée peut être stockée dans une variable. ✅
- Les fonctions avec un type renvoyé `Unit` doivent inclure une instruction `return`.
- Une valeur renvoyée doit être du même type que celui renvoyé par une fonction. ✅

#### 9. Quelles affirmations concernant les fonctions sont vraies ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- Les fonctions acceptent des paramètres ou des variables en tant qu'entrées. ✅
- Les paramètres de fonction doivent avoir des arguments par défaut.
- Lorsque vous appelez une fonction avec des paramètres, les valeurs transmises sont appelées "arguments". ✅
- Diviser votre code en fonctions distinctes facilite sa gestion. ✅

#### 10. Les arguments nommés vous permettent de modifier l'ordre dans lequel vous transmettez les arguments à une fonction.

- Vrai ✅
- Faux

### Configurer Android Studio

#### 1. Que signifie IDE ?

- Integrated Development Environment ✅
- Independent Design Environment
- Ideal Developer Environment
- Intelligent Design Environment

#### 2. Quels sont les avantages d'Android Studio ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- Il permet d'éviter les fautes de frappe et les autres erreurs figurant dans votre code. ✅
- Il est fourni avec un appareil virtuel (appelé émulateur) capable d'exécuter votre application. ✅
- Il peut vous montrer un aperçu en temps réel de l'aspect de votre application à l'écran pendant que vous codez. ✅
- Il peut traduire automatiquement votre application dans d'autres langues.

#### 3. Quel est l'intérêt d'utiliser un appareil virtuel (ou émulateur) dans Android Studio ?

- Pour afficher divers messages d'erreur aux utilisateurs
- Pour tester le code de l'application de manière sécurisée
- Pour tester votre application sur un appareil sans disposer de cet appareil physique ✅
- Pour voir à quoi ressemble votre application dans un navigateur Web

#### 4. À quoi sert un modèle de projet dans Android Studio ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- Il permet à Android Studio de télécharger les fichiers plus rapidement.
- Il permet de créer plus rapidement une application. ✅
- Il offre une structure conforme aux bonnes pratiques. ✅
- C'est le seul moyen de créer des applications que vous pouvez prévisualiser dans Android Studio.
- Il permet de réduire les risques d'erreur lors de la création d'une application en préremplissant le projet avec du code d'application. ✅

#### 5. Comment créer un projet dans Android Studio ?

- A. Déconnectez-vous d'Android Studio, puis accédez au dossier de votre projet pour savoir comment procéder.
- B. Si vous avez déjà ouvert un projet, sélectionnez Fichier > Nouveau > Nouveau projet dans le menu Android Studio.
- C. Dans la fenêtre Bienvenue dans Android Studio, cliquez sur Démarrer un nouveau projet Android Studio.
- D. Créez un fichier sur votre ordinateur et nommez-le "Nouveau projet Android Studio".
- B et C permettent de créer un projet dans Android Studio. ✅
- Aucune des réponses ci-dessus

#### 6. ___ est une fonction permettant de définir une mise en page dans votre application à l'aide de fonctions modulables.

- `ComponentActivity()`
- `onCreate()`
- `DefaultPreview()`
- `setContent()` ✅

#### 7. Une fonction Compose nécessite l'annotation @Composable.

- Vrai ✅
- Faux

#### 8. Un ___ est un composable avec une couleur d'arrière-plan qui peut contenir d'autres composables.

- Color
- Container
- Surface ✅
- Box

#### 9. La marge intérieure est un exemple d'/de ___

- propriété
- composable
- attribut
- modificateur ✅

#### 10. Quelle affirmation concernant Compose est fausse ?

- Le modèle Activité Compose vide permet de créer une application simple.
- Vous pouvez afficher les mises en page dans la fenêtre d'aperçu, sans exécuter votre application.
- Tous les éléments et thèmes d'une application Compose sont contenus dans une surface. ✅
- Les thèmes, tels que `GreetingCardTheme`, vous permettent de définir le style des composables.

### Créer une mise en page de base

#### 1. Qu'est-ce que Jetpack Compose ?

- Un kit d'outils modernes pour développer des interfaces utilisateur Android ✅
- Un kit d'outils pour concevoir des bibliothèques
- Une interface de base de données
- Un plug-in de développement d'APK

#### 2. Les fonctions modulables sont les éléments de base de Compose.
- Vrai ✅
- Faux

#### 3. Quel élément permet d'annoter une fonction composable ?

- `@Annotation`
- `@ComposableFunction`
- `@Composable` ✅
- `@Preview`

#### 4. Dans Compose, les éléments de mise en page de base sont :
*Choisissez autant de réponses que vous jugez nécessaires.*

- Column ✅
- Row ✅
- Text
- Box ✅

#### 5. Quelle fenêtre d'outil permet d'importer, de créer, de gérer et d'utiliser des ressources dans votre application ?

- Gestionnaire d'applications
- Resource Manager ✅
- Outil de ressources
- Gestionnaire de mises en page

#### 6. Quelle classe est générée automatiquement par Android et contient les ID de toutes les ressources du projet ?

- La classe `Android`
- La classe `Resource`
- La classe `R` ✅
- La classe `ResourceID`

#### 7. Quelle fonction permet de charger une ressource d'image drawable ?

- La fonction `stringResource()`
- La fonction `painterResource()` ✅
- La fonction `ImageResource()`
- La fonction `loadResource()`

#### 8. Quel paramètre de fonction sert à ajouter un texte d'accessibilité, utilisé par TalkBack ?

- `accessibilityText`
- `contentText`
- `accessibilityDescription`
- `contentDescription` ✅

#### 9. La mise en page Box empile les éléments d'interface utilisateur les uns sur les autres.

- Vrai ✅
- Faux

#### 10. Quel paramètre permet d'aligner l'élément enfant avec le début du parent ?

- `Alignment.End`
- `Alignment.Begin`
- `Alignment.Start` ✅
- `Alignment.Top`

## Module 2 : Créer l'interface utilisateur d'une application

### Principes de base de Kotlin

#### 1. Le code suivant affichera "Divisible by 5" si number est égal à 25.

```kotlin
if (number % 10 == 0) {
  println("Divisible by 10")
} else if (number == 5) {
  println("Divisible by 5")
}
```

- `true`
- `false` ✅

#### 2. Parmi les conditions suivantes, lesquelles sont remplies lorsque `x = 5` ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- `x == 5` ✅
- `x in 1..5` ✅
- `x is Int` ✅
- `x % 5`

#### 3. Parmi les propositions suivantes, laquelle n'est pas un concept de base de la programmation orientée objet ?

- Abstraction
- Lisibilité ✅
- Héritage
- Polymorphisme

#### 4. Quels sont les quatre modificateurs de visibilité en Kotlin ?

- `public`, `private`, `protected`, `abstract`
- `static`, `override`, `internal`, `external`
- `private`, `protected`, `public`, `internal` ✅
- `public`, `protected`, `static`, `internal`

#### 5. Le mot clé ___ est utilisé pour appeler une méthode à partir de la classe parent.

- `this`
- `super` ✅
- `parent`
- `self`

#### 6. Un(e) ___ définit les propriétés ou les méthodes devant être implémentées par une classe.

- délégué
- type générique
- interface ✅
- sous-classe

#### 7. Parmi les éléments suivants, lequel est le mieux représenté par un type nullable ?

- Le nombre de followers (zéro ou plus) dans une application de réseaux sociaux.
- Une photo de profil facultative. ✅
- Un nom d'utilisateur devant comporter au moins un caractère.
- Un identifiant unique attribué à chaque utilisateur.

#### 8. L'opérateur ___ vous permet d'appeler une méthode uniquement si l'objet n'est pas nul.

- `.`
- `!!`
- `?:`
- `?.` ✅

#### 9. Parmi les affirmations suivantes concernant les fonctions Kotlin, laquelle est fausse ?

- Une fonction peut être remplacée par un autre type de données, et inversement. ✅
- Une fonction peut être renvoyée à partir d'une autre fonction.
- Une fonction peut en utiliser une autre en tant que paramètre.
- Une fonction possède un type de données, tel que `(Int) -> Unit`.

#### 10. Un littéral de fonction est un autre nom pour désigner ___

- un type de fonction
- une expression lambda ✅
- une référence de fonction
- une lambda finale

### Ajouter un bouton à une application

#### 1. Utilisez un composable ___ pour afficher une image.

- Button
- Text
- Image ✅
- Icon

#### 2. `Alignment.Center` centre les composants de l'interface utilisateur horizontalement et verticalement.

- Vrai ✅
- Faux

#### 3. Les fonctions modulables peuvent stocker un objet en mémoire à l'aide du composable ___.

- remember ✅
- Column
- Modifier
- @Composable

#### 4. Le débogueur vous permet d'inspecter les variables lorsque l'exécution du code a été suspendue.

- Vrai ✅
- Faux

#### 5. En utilisant des valeurs ___ dans une fonction modulable, vous pouvez transformer les variables en objets observables qui planifient une recomposition lorsque leur valeur change.

- remember
- Modifier
- @Composable
- mutableStateOf ✅

#### 6. Le composable ___ place ses enfants dans une séquence verticale.

- Row
- Box
- Column ✅
- Modifier

#### 7. La fonctionnalité de débogueur ___ vous permet de remonter dans la pile d'appel.

- Passer
- Sortir ✅
- Entrer
- Reprendre le programme

### Interagir avec l'interface utilisateur et l'état

#### 1. Lorsque Jetpack Compose exécute vos composables pour la première fois lors du/de la ___, il suit les composables que vous appelez pour décrire votre UI.

- composition initiale ✅
- recomposition
- changement d'état
- fermeture de l'application

#### 2. Le seul moyen de modifier une composition est la recomposition.

- Vrai ✅
- Faux

#### 3. Le/La ___ désigne le moment où Jetpack Compose réexécute les composables qui ont pu changer en réponse à des modifications de données.

- composition initiale
- recomposition ✅
- changement d'état
- fermeture de l'application

#### 4. Dans une application, l'/le/la ___ correspond à toute valeur susceptible de changer au fil du temps.

- état ✅
- valeur
- valueChange
- StateValue

#### 5. Le/La ___ est un modèle qui consiste à faire remonter un état pour obtenir un composant sans état.

- changement d'état
- hissage d'état ✅
- composition de hissage
- recomposition

#### 6. Quelle propriété `KeyboardAction` permet de déplacer le curseur vers le composable suivant ?

- `onDone`
- `onNext` ✅
- `onGo`
- `onSend`

#### 7. Quelle fonction Kotlin permet d'arrondir une valeur de type float ou double ?

- `kotlin.math.ceilUp()`
- `kotlin.math.ceil()` ✅
- `kotlin.math.roundDown()`
- `kotlin.math.roundUp()`

#### 8. L'outil d'inspection de la mise en page, disponible dans Jetpack Compose, permet d'inspecter une mise en page Compose dans une application en cours d'exécution sur un émulateur ou un appareil physique.

- Vrai ✅
- Faux

#### 9. Les tests de l'interface utilisateur sont enregistrés dans le répertoire ___.

- main
- androidTest ✅
- test
- res

#### 10. Les tests locaux et les tests de l'interface utilisateur doivent être annotés avec l'annotation ___.

- `@VisibleForTesting`
- `@Preview`
- `@Test` ✅
- `@Composable`

## Module 3 : Afficher des listes et utiliser Material Design

### Autres principes de base de Kotlin

#### 1. Parmi les propositions suivantes, laquelle permet de définir une classe de données en Kotlin ?

- `data class Person(val name: String, val age: Int)` ✅
- `class Person(val name: String, val age: Int): data`
- `class Person(val name: String, val age: Int)`
- `data class Person{val name: String, val age: Int}`

#### 2. Lorsque vous utilisez une classe scellée, toutes les sous-classes directes doivent se trouver dans le même package.

- Vrai ✅
- Faux

#### 3. Lorsque vous utilisez des génériques, le type de données "générique" est inclus dans ___.

- `[]`
- `{}`
- `()`
- `<>` ✅

#### 4. Une classe ___ est utile lorsque vous possédez un ensemble fixe de valeurs.

- enum ✅
- scellée
- de données
- héritée

#### 5. Pour créer un objet de liste capable de modifier sa taille, vous devez appeler ___.

- `modifiableListOf()`
- `immutableListOf()`
- `listOf()`
- `mutableListOf()` ✅

#### 6. Parmi les propositions suivantes, lesquelles sont des fonctions d'ordre supérieur ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- `map` ✅
- `arrangeBy`
- `filter` ✅
- `forEach` ✅

#### 7. Compte tenu de la ligne de code suivante et parmi les commandes proposées, laquelle permettra d'imprimer Blue ? (Conseil : En cas de doute, essayez d'exécuter le code en Kotlin Playground.)

```kotlin
val colors = listOf("Red", "Green", "Blue")
```
*Choisissez autant de réponses que vous jugez nécessaires.*

- `println(colors[2])` ✅
- `println(colors.get(2))` ✅
- `println(colors.contains(2))`
- `println(colors.getOrDefaultValue(index = 2, defaultValue = 10))`

#### 8. Le concept de programmation d'une classe comportant une seule instance est appelé "___".

- unicité
- singleton ✅
- objet unique
- lambda

#### 9. Parmi les affirmations suivantes concernant les ensembles et les cartes, laquelle est vraie ?

- Un ensemble doit contenir des valeurs distinctes et les clés d'une carte doivent être distinctes. ✅
- Un ensemble doit contenir des valeurs distinctes et les clés d'une carte peuvent contenir des doublons.
- Un ensemble peut contenir des valeurs en double, les valeurs d'une carte également.
- Un ensemble peut contenir des valeurs en double et les clés d'une carte doivent être distinctes.

#### 10. Si vous disposez d'une variable nommée `records`, qui est une collection, vous pouvez appeler ___ afin de déterminer le nombre d'éléments qu'elle contient.

- `records.length`
- `records.quantity`
- `len(records)`
- `records.size` ✅

### Créer une liste déroulante

#### 1. Les icônes de lanceur adaptatives des applications Android se composent d'un drawable vectoriel de premier plan et d'arrière-plan.

- Vrai ✅
- Faux

#### 2. Quel composable permet de créer une liste déroulante avec un nombre variable d'éléments ?

- `Column`
- `Row`
- `LazyColumn` ✅
- `Card`

#### 3. Quel type de fichier est utilisé pour les vecteurs de premier plan et d'arrière-plan de l'icône de lanceur ?

- .txt
- .jpg
- .png
- .xml ✅

#### 4. Quel composable permet de créer une grille à défilement vertical avec un nombre indéterminé d'éléments ?

- `LazyColumn`
- `LazyVerticalGrid` ✅
- `LazyHorizontalGrid`
- `Row`

#### 5. Le composable `Column` n'est pas une bonne option pour une liste d'éléments de longueur inconnue, car ___.

- il ne peut contenir qu'un nombre limité d'éléments prédéfinis. ✅
- il organise les éléments verticalement.
- il active le défilement par défaut, sans code supplémentaire.
- il peut ajouter du contenu à la demande.

#### 6. La méthode ___ permet d'ajouter du contenu à un composable LazyColumn.

- `painterResource()`
- `Modifier.padding()`
- `items()` ✅
- `onCreate()`

#### 7. Quel composable organise les éléments horizontalement ?

- `Column`
- `Card`
- `Image`
- `Row` ✅

#### 8. Quel composable organise les éléments verticalement ?

- `Column` ✅
- `Card`
- `Image`
- `Row`

### Concevoir des applications attrayantes

#### 1. En ajoutant des animations dans votre application Android, vous pouvez :

- Indiquer visuellement ce qui se passe dans votre application.
- Donner une apparence soignée à votre application.
- Signaler des modifications.
- Toutes les réponses ci-dessus ✅

#### 2. L'animation du ressort est basée sur :
- Les valeurs de début et de fin sur la durée spécifiée.
- Le taux d'amortissement et la raideur. ✅
- Les valeurs d'instantané spécifiées à différents horodatages.
- Une interpolation entre deux valeurs d'image clé.

#### 3. L'animation du ressort est basée sur le principe physique de la force de ressort.

- Vrai ✅
- Faux

#### 4. Dans la thématisation Material, la couleur ___ correspond à la couleur la plus fréquente sur les écrans et dans les composants de votre application.

- principale ✅
- secondaire
- de surface
- d'arrière-plan

#### 5. Le fichier suivant est utilisé pour définir les formes des composants dans Compose.

- `Theme.kt`
- `Color.kt`
- `Shape.kt` ✅
- `Colors.kt`

#### 6. Vous ne pouvez avoir qu'un seul composable @Preview

- Vrai
- Faux ✅

#### 7. Un code couleur hexadécimal commence par le caractère dièse (#), suivi de six lettres et/ou chiffres représentant les composants rouge, vert et bleu (RVB) de cette couleur.

- Vrai ✅
- Faux

#### 8. Le fichier ___ contient toutes les informations sur le thème de l'application, lequel est défini par des couleurs, des formes et une typographie.

- Theme.kt ✅
- Color.kt
- Shape.kt
- Colors.kt

#### 9. L'/Le/La ___ crée un contraste entre la fiche et l'arrière-plan en ajoutant une ombre qui rend l'application plus réaliste et plus attrayante.

- élévation ✅
- forme
- couleur
- thème

#### 10. Quels sont les avantages du thème sombre ?

- Il peut réduire considérablement la consommation d'énergie (selon la technologie d'écran de l'appareil).
- Il améliore la visibilité pour les utilisateurs souffrant d'une déficience visuelle et ceux sensibles à la lumière vive.
- Il permet à tous d'utiliser un appareil dans des conditions de faible luminosité.
- Toutes les réponses ci-dessus ✅

#### 11. TalkBack permet de naviguer dans une application en utilisant des contacteurs au lieu de l'écran tactile.

- Vrai
- Faux ✅

#### 12. Quel attribut permet à TalkBack d'énoncer une description pertinente d'une image ou d'une icône ?

- `elevation`
- `shape`
- `contentDescription` ✅
- `style`

## Module 4 : Navigation et architecture des applications

### Composants de l'architecture

#### 1. Quelle méthode est appelée en premier lorsque l'application n'est plus active ?

- onPause() ✅
- onStart()
- onCreate()
- onStop()

#### 2. Après ___, l'application ne sera plus visible à l'écran.

- onPause()
- onStart()
- onCreate()
- onStop() ✅

#### 3. Utilisez ___ pour rédiger un message de débogage. Cette méthode nécessite deux arguments : la balise de journal et le message de journal.

- `Log.i()`
- `Log.d()` ✅
- `Log.e()`
- `Log.w()`

#### 4. Pour enregistrer une valeur devant survivre à une modification de configuration, déclarez ses variables avec ___.

- `MutableState{}`
- `rememberSaveable{}` ✅
- `remember{}`
- Hissage d'état

#### 5. Selon le principe de conception de séparation des tâches, l'application doit être divisée en classes, chacune ayant des responsabilités distinctes.

- Vrai ✅
- Faux

#### 6. L'interface utilisateur correspond à ce que l'utilisateur voit, tandis que l'état de l'interface utilisateur correspond à ce qu'il devrait voir selon l'application.

- Vrai ✅
- Faux

#### 7. Selon l'architecture d'application recommandée, chaque application doit au minimum comporter les deux couches suivantes :

- Couches de domaine et de données
- Couches d'interface utilisateur et de données ✅
- Couches de dépôt et d'interface utilisateur
- Couches de domaine et d'interface utilisateur

#### 8. `StateFlow` est un flux observable de conteneur de données qui émet les mises à jour de l'état actuel et du nouvel état.

- Vrai ✅
- Faux

#### 9. Parmi les configurations suivantes, laquelle doit être ajoutée au fichier `build.gradle` afin d'ajouter des dépendances au code source du test unitaire ?

- `implementation`
- `testImplementation` ✅
- `debugImplementation`
- `androidTestImplementation`

#### 10. Les tests unitaires sont exécutés sur un émulateur ou un appareil Android.

- Vrai
- Faux ✅

### Navigation dans Jetpack Compose

#### 1. Un itinéraire est défini avec un type de données ___.

- Fonction `@Composable`
- `NavHost.Route`
- `String` ✅
- `NavRoute`

#### 2. Avec `NavHost`, vous devez explicitement spécifier un écran de démarrage.

- Vrai ✅
- Faux

#### 3. Il est recommandé de ne pas transmettre un `NavHostController` à des composables individuels.

- Vrai ✅
- Faux

#### 4. ___ est un composable qui gère l'écran qui s'affiche en fonction d'une route donnée.

- `NavController`
- `NavHostController`
- `NavHost` ✅
- `ComposableNavigator`

#### 5. Parmi les paramètres suivants, quels sont les deux pris par la fonction `composable()` appelée dans un `NavHost` ?

- Un contenu de destination et une route
- Une route et un contenu modulable ✅
- Un chemin d'accès et un composable
- Un contenu modulable et un intent.

#### 6. Vous pouvez modifier la route actuellement affichée à l'aide de la méthode ___.

- `update()`
- `composable()`
- `transition()`
- `navigate()` ✅

#### 7. La méthode ___ permet de supprimer un ou plusieurs écrans de la pile "Retour".

- `popToStartDestination()`
- `popBackStack()` ✅
- `popComposable()`
- `popToBackStack()`

#### 8. Dans une application multi-écran, le fait d'accéder à un nouvel écran place celui-ci au bas de la pile "Retour".

- Vrai
- Faux ✅

#### 9. L'intent ___ contient des données supplémentaires transmises à un intent.

- arguments
- extras ✅
- parameters
- properties

#### 10. `StateFlow` est un flux observable de conteneur de données qui émet les mises à jour de l'état actuel et du nouvel état.

- Vrai ✅
- Faux

#### 11. Parmi les affirmations suivantes concernant les boutons "Retour" et "Haut", lesquelles sont vraies ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- Le bouton "Retour" est un bouton système. ✅
- Le bouton "Haut" est fourni par le système en bas de l'écran.
- Le bouton "Retour" fait partie de l'`AppBar`
- Le bouton "Haut" de l'`AppBar` permet de revenir automatiquement à l'écran précédent.
- Le bouton "Retour" ne s'affiche que si vous utilisez la navigation.
- Le bouton "Haut" peut être affiché ou masqué selon l'écran actuel. ✅

### S'adapter à différentes tailles d'écran

#### 1. Le composable ___ est utilisé pour répondre au bouton "Retour", avec ou sans `NavHost`.

- `BackButton`
- `BackHandler` ✅
- `BackNavigator`
- `BackStack`

#### 2. Parmi les affirmations suivantes concernant les écrans plus grands, lesquelles sont vraies ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- Le positionnement des boutons est plus important sur les écrans plus grands. ✅
- Il n'est généralement pas nécessaire de modifier la mise en page de l'interface utilisateur pour que l'application fonctionne bien sur les grands écrans.
- Ajouter une autre mise en page sur le même écran évite d'avoir à naviguer entre les écrans. ✅
- Les mises en page pour grands écrans doivent éviter de regrouper les boutons les plus utilisés au centre de l'écran. ✅

#### 3. ___ est une mesure spécifique de la largeur ou de la hauteur, où la mise en page d'une application doit changer.

- Une classe de fenêtre
- Un point de mise en page
- Un bucket de tailles
- Un point d'arrêt ✅

#### 4. La classe de taille de fenêtre de largeur compacte fait généralement référence à des appareils plus petits, comme des téléphones en mode Portrait.

- Vrai ✅
- Faux

#### 5. L'API ___ simplifie l'implémentation des mises en page adaptatives.

- `SizeClass`
- `WindowSizeState`
- `SizeBucket`
- `WindowSizeClass` ✅

#### 6. Un rail de navigation convient souvent aux mises en page de largeur ___.

- compacte
- standard
- moyenne ✅
- agrandie

#### 7. Lorsque vous créez des applications avec des mises en page adaptatives, vous ne devez utiliser qu'un seul aperçu pour chaque écran.

- Vrai
- Faux ✅

#### 8. La mise en page "list-detail" nécessite un retour en arrière sur les écrans de petit format, mais pas sur ceux affichant simultanément la liste et les écrans détaillés.

- Vrai ✅
- Faux

#### 9. Supposons que vous ayez une application de contacts qui affiche une liste de contacts et dispose d'informations complémentaires à afficher pour chaque contact. Comment faire pour adapter l'interface utilisateur à différentes tailles d'écran ?

- Utilisez la mise en page "list-detail" pour afficher un ou deux volets côte à côte en fonction de la largeur d'écran disponible. ✅
- Les éléments de la liste doivent occuper toute la largeur de l'écran, indépendamment de sa largeur.
- Le bouton "Haut" doit toujours s'afficher dans l'application. Tout clic sur ce bouton doit permettre de quitter l'application.
- Lorsque vous faites pivoter l'appareil, l'élément sélectionné dans la liste (et les informations correspondantes qui s'affichent) doit être réinitialisé pour devenir le premier élément de la liste.
- Il est nécessaire d'utiliser le composant Navigation de Jetpack pour que l'interface utilisateur s'adapte à diverses tailles d'écran.

#### 10. Vous pouvez configurer les tests pour qu'ils n'exécutent que des fonctions de test avec des annotations personnalisées en configurant ___.

- le module
- le package
- la classe Instrumentation
- les arguments Instrumentation ✅

## Module 5 : Se connecter à Internet

### Récupérer des données sur Internet

#### 1. Avec la programmation simultanée, le code peut s'exécuter dans un ordre différent de celui dans lequel il a été écrit.

- Vrai ✅
- Faux

#### 2. Complétez la phrase
*Saisissez un ou plusieurs mots pour compléter la phrase.*

Le thread **principal** est chargé d'afficher l'interface utilisateur répondant aux entrées utilisateur.

#### 3. Parmi les affirmations suivantes concernant les contextes de coroutine, lesquelles sont vraies ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- `Dispatchers.Default` est le meilleur choix pour les tâches de longue durée impliquant la lecture et l'écriture de grandes quantités de données.
- `Dispatchers.Main` peut être utilisé pour mettre à jour l'interface utilisateur, mais pas pour les tâches de longue durée. ✅
- `Job` contrôle le cycle de vie d'une coroutine. ✅
- `Dispatchers.IO` est optimisé pour les E/S réseau, entre autres tâches en arrière-plan. ✅

#### 4. `launch()` et `async()` sont des fonctions d'extension de ___, qui effectue le suivi des coroutines qu'il crée.

- `CoroutineScope` ✅
- `Job`
- `Dispatcher`
- `CoroutineContext`

#### 5. Parmi les affirmations suivantes concernant la simultanéité structurée, lesquelles sont vraies ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- Si une coroutine est annulée, les coroutines enfants doivent également être annulées. ✅
- Un champ d'application parent peut être terminé avant qu'un ou plusieurs de ses enfants ne le soient.
- Un échec doit se propager vers le bas sans annuler la coroutine parente.
- Les coroutines doivent être lancées à partir d'un champ d'application de coroutine. ✅

#### 6. Parmi les affirmations suivantes concernant les services Web, lesquelles sont vraies ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- GET, POST et DELETE sont tous des exemples d'opérations HTTP. ✅
- Une URL est un type d'URI, mais tous les URI ne sont pas des URL. ✅
- Les services RESTful fournissent toujours une réponse au format XML.
- Retrofit est une bibliothèque tierce qui permet de gérer JSON à partir d'un service Web.

#### 7. Retrofit est une bibliothèque tierce qui permet à votre application d'envoyer des requêtes à un service Web ___.

- XML
- Socket
- RESTful ✅
- JSON

#### 8. Une méthode recommandée pour effectuer une requête réseau Retrofit consiste à lancer une coroutine dans viewModelScope.

- Vrai ✅
- Faux

#### 9. Pour autoriser votre application à se connecter à Internet, ajoutez l'autorisation `android.permission.INTERNET` dans le fichier ___.

- `MainActivity`
- `build.gradle`
- Fichier manifeste Android ✅
- `ViewModel`

#### 10. Le processus qui consiste à transformer un résultat JSON en données utilisables, comme c'est le cas avec Gson, est appelé JSON ___.

- Serialization
- Encoding
- Converting
- Parsing ✅

### Charger et afficher des images depuis Internet

#### 1. Laquelle de ces méthodes ou opérations HTTP n'est pas courante ?

- GET
- Requêtes POST
- DELETE
- SET ✅

#### 2. La réponse d'un service Web REST est couramment formatée dans l'un des formats de transfert de données courants tels que XML ou JSON.

- Vrai ✅
- Faux

#### 3. Parmi les affirmations suivantes concernant la bibliothèque Retrofit, laquelle est fausse ?

- Il s'agit d'une bibliothèque cliente.
- Elle permet à votre application d'envoyer des requêtes à un service Web REST.
- Elle convertit les objets Kotlin en objets JSON. ✅
- Il s'agit d'une bibliothèque tierce.

#### 4. Parmi les propositions suivantes, laquelle s'applique à un modèle Singleton ?

- Les déclarations `object` sont utilisées pour déclarer des objets singleton dans Kotlin.
- S'assure qu'une seule et unique instance d'un objet est créée
- Dispose d'un point d'accès global à cet objet.
- Toutes les réponses ci-dessus ✅

#### 5. Chaque objet JSON contient les éléments suivants :

- Un ensemble de paires clé-valeur séparées par le signe deux-points.
- Un ensemble de paires clé-valeur séparées par une virgule. ✅
- Un ensemble de paires clé-valeur séparées par un point-virgule.
- Aucune des propositions ci-dessus

#### 6. Conformément aux consignes d'architecture recommandées pour Android, une application doit contenir les éléments suivants :

- Une couche d'UI
- Une couche de domaine
- Une couche de données ✅
- Une couche d'entreprise

#### 7. Quels sont les avantages de l'injection de dépendances (DI) dans votre application ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- Aide à la réutilisation du code ✅
- Facilite la refactorisation ✅
- Aide avec les tests ✅
- Rend votre application plus rapide

#### 8. Si votre application comporte plusieurs types de sources de données, elles doivent toutes être stockées dans le même dépôt pour plus de simplicité.

- Vrai
- Faux ✅

#### 9. Parmi les éléments suivants, lequel permet de remplacer le coordinateur `Main` par `TestDispatcher` dans un test unitaire local ?

- `runTest`
- `runBlocking`
- `Distpatchers.resetMain()`
- `Dispatchers.setMain()` ✅

#### 10. La fonction `runTest()` peut être utilisée pour tester les fonctions `suspend`.

- Vrai ✅
- Faux

## Module 6 : Persistance des données

### Présentation de SQL

#### 1. Parmi les affirmations suivantes concernant les bases de données relationnelles et SQLite, lesquelles sont vraies ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- Le référencement de la clé primaire d'une table dans une autre vous permet de modéliser les relations entre les tables. ✅
- Une base de données SQLite est composée de colonnes, elles-mêmes composées de tables et de lignes.
- Chaque table de données doit comporter au moins une clé étrangère.
- Les lignes contiennent les éléments individuels de la base de données. ✅

#### 2. Il est facultatif de terminer une instruction SQL par un point-virgule.

- Vrai
- Faux ✅

#### 3. Si vous souhaitez calculer la somme de toutes les valeurs d'une colonne de base de données, qu'utilisez-vous ?

- Une fonction d'agrégation ✅
- `WHERE clause`
- Un mot clé `DISTINCT`
- Une clause `LIMIT`

#### 4. Quelle instruction SELECT renvoie le nombre d'adresses e-mail uniques des messages dans le dossier de spam ?

- `SELECT COUNT(DISTINCT folder) FROM email WHERE spam != sender;`
- `SELECT DISTINCT COUNT(sender) FROM email WHERE folder = 'spam';`
- `SELECT COUNT(DISTINCT sender) FROM email WHERE folder = 'spam';` ✅
- `SELECT DISTINCT COUNT('spam') FROM email WHERE sender = folder;`

#### 5. L'instruction SQL `SELECT * FROM contacts WHERE name LIKE '%Milton'` renvoie toutes les lignes dont la valeur de la colonne "name" commence par `Milton`.

- Vrai
- Faux ✅

#### 6. Parmi les affirmations suivantes concernant `GROUP BY` et `ORDER BY`, lesquelles sont vraies ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- La clause `ORDER BY` précède la clause `GROUP BY`.
- Dans une clause `ORDER BY`, l'ordre décroissant est sélectionné par défaut. ✅
- Si une requête contient une clause `GROUP BY`, elle remplace la clause `ORDER BY`.
- Les clauses `ORDER BY` et `GROUP BY` peuvent toutes deux accepter plusieurs colonnes. ✅

#### 7. La condition `WHERE NOT read = false` et la condition `WHERE read != true` sont équivalentes.

- Vrai
- Faux ✅

#### 8. La clause `LIMIT` `LIMIT 30 SKIP 60` renvoie :

- 60 lignes
- Les lignes 31 à 60
- Les lignes 61 à 90 ✅
- 90 lignes

#### 9. Une instruction `UPDATE` utilise une clause ___ pour attribuer des valeurs aux colonnes.

- `WHERE`
- `SET` ✅
- `ASSIGN`
- `LIKE`

#### 10. Les instructions `UPDATE` et `DELETE` peuvent inclure une clause WHERE et peuvent affecter plusieurs lignes.

- Vrai ✅
- Faux

### Utiliser Room pour la persistance des données

#### 1. Parmi les affirmations suivantes concernant l'annotation `@Query`, laquelle est fausse ?

- L'annotation `@Query` est utilisée avec une méthode dans la DAO.
- L'annotation `@Query` correspond à une requête `SELECT`.
- L'annotation `@Query` peut transmettre des arguments dans une instruction SQL en plaçant deux points avant son nom.
- L'annotation `@Query` ne peut être utilisée qu'avec une fonction de suspension. ✅

#### 2. Parmi les affirmations suivantes concernant la DAO, lesquelles sont vraies ?

- Les fonctions DAO utilisent des annotations telles que `@Insert` et `@Update`, qui correspondent à une opération sur la base de données.
- Les fonctions DAO peuvent renvoyer un flux.
- Les instances de classes DAO sont référencées dans la classe `AppDatabase`.
- Toutes les réponses ci-dessus ✅

#### 3. La classe Database, héritant de la classe RoomDatabase, est chargée ___.

- D'instancier la base de données et fournir l'accès au DAO ✅
- De représenter des tables de données individuelles.
- De définir des fonctions correspondant aux instructions SQL, telles que les requêtes `SELECT`.
- De fournir des données à l'interface utilisateur.

#### 4. Le DAO sert à :

- Conserver la référence aux modèles de vues et à la base de données.
- Définir des fonctions correspondant aux instructions SQL, telles que les requêtes `SELECT` et `INSERT`. ✅
- Fournir une méthode de fabrique pour créer une instance de base de données.
- Créer une instance de base de données.

#### 5. Pourquoi devez-vous utiliser la fonction `synchronized()` lorsque vous créez la base de données ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- Elle vous permet de créer plusieurs copies de la base de données.
- Elle vous permet d'accéder simultanément et de manière sécurisée au code de plusieurs threads. ✅
- Elle permet d'éviter les conditions de concurrence. ✅
- Elle garantit qu'un seul thread à la fois peut entrer dans le bloc de code. ✅

#### 6. Vous pouvez utiliser les annotations `@Insert` et `@Delete` sans fournir d'instruction SQL.

- Vrai ✅
- Faux

#### 7. Complétez la phrase
*Saisissez un ou plusieurs mots pour compléter la phrase.*

Pour gérer les conflits pouvant survenir lors de l'insertion dans une base de données, vous pouvez transmettre un paramètre **onConflict**, tel que IGNORE, à l'annotation @Insert.

#### 8. Sélectionnez toutes les affirmations vraies concernant l'outil d'inspecteur de bases de données :
*Choisissez autant de réponses que vous jugez nécessaires.*

- Il vous permet d'inspecter, d'interroger et de modifier les bases de données de votre application pendant son exécution. ✅
- Il fonctionne avec d'autres bibliothèques SQLite que vous intégrez à votre application.
- Il est particulièrement utile pour déboguer des bases de données. ✅
- Il fonctionne avec SQLite standard et avec des bibliothèques basées sur SQLite, telles que Room. ✅

#### 9. Les entités représentent des tables de données individuelles dans la base de données Room.

- Vrai ✅
- Faux

#### 10. Parmi les affirmations suivantes concernant la clé primaire, laquelle est fausse ?

- Vous pouvez utiliser la clé primaire pour identifier de manière unique chaque enregistrement/entrée dans vos tables de la base de données.
- Une fois la clé primaire attribuée, vous ne pouvez plus la modifier.
- Room génère par défaut une valeur de clé primaire incrémentée pour chaque entité. ✅
- La clé primaire représente l'objet de l'entité tant qu'il existe dans la base de données.

### Stocker des données et y accéder à l'aide de clés avec DataStore

#### 1. Les implémentations de `DataStore` sont les suivantes :
*Choisissez autant de réponses que vous jugez nécessaires.*

- Proto ✅
- Preferences ✅
- Room
- SQLite

#### 2. Preferences DataStore utilise un schéma prédéfini.

- Vrai
- Faux ✅

#### 3. Quelle est la fonction fournie par DataStore pour modifier le DataStore ?

- preferencesDataStore()
- updatePreferences()
- edit() ✅
- map()

#### 4. Preferences DataStore utilise des clés pour accéder aux valeurs stockées.
- Vrai ✅
- Faux

#### 5. Quelle exception peut se produire lorsque vous tentez de lire les données d'un Preferences DataStore ?

- IllegalArgumentException
- IOException ✅
- IllegalStateException
- NumberFormatException

## Module 7 : WorkManager

### Planifier des tâches avec WorkManager

#### 1. Quel outil vous permet de visualiser, de surveiller et de déboguer les Workers de votre application ?

- Profiler
- Background Task Inspector ✅
- Logcat
- Gestionnaire d'appareils

#### 2. Parmi les options suivantes, lesquelles sont des états de fonctionnement terminal valides ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- CANCELLED ✅
- DELETED
- FAILED ✅
- SUCCEEDED ✅

#### 3. Parmi les options suivantes, laquelle est un type de demande de travail valide ?
*Choisissez autant de réponses que vous jugez nécessaires.*

- `OneTimeWorkRequest` ✅
- `SingleWorkRequest`
- `RepeatingWorkRequest`
- `PeriodicWorkRequest` ✅

#### 4. La création et l'ajout à la file d'attente de plusieurs tâches dépendantes, ainsi que l'ordre dans lequel elles doivent s'exécuter, est appelé "association".

- Vrai
- Faux ✅

#### 5. Parmi les options suivantes, dans quelle situation les contraintes de travail sont-elles utiles ?

- Pour vérifier qu'un mode de paiement valide est enregistré sur l'appareil de l'utilisateur avant que le travail ne soit effectué.
- Pour vérifier l'heure avant l'exécution du travail.
- Pour vérifier que l'appareil est connecté à un réseau Wi-Fi avant de télécharger une grande quantité de données d'application. ✅
- Pour vérifier que l'application a été ouverte un certain nombre de fois avant l'exécution du travail.

#### 6. Parmi les options suivantes, laquelle permet de transmettre des données d'entrée à un Worker ?

- Transmettre les données en tant qu'argument lorsque vous appelez la fonction `doWork()`.
- Utiliser un objet Data pour transmettre des paires clé/valeur. ✅
-Transmettre les données en tant que String, mais elles doivent comporter moins de 140 caractères.
- L'attribuer à la variable `worker.inputData`.

#### 7. Une fois le travail ajouté à la file d'attente, vous pouvez vérifier son état par ___.
*Choisissez autant de réponses que vous jugez nécessaires.*

- Nom ✅
- ID ✅
- Balise ✅
- WorkType

#### 8. Le Background Task Inspector vous permet d'arrêter les Workers pendant leur exécution.

- Vrai
- Faux ✅

#### 9. Quel compilateur de workers est recommandé pour tester les `CoroutineWorkers` ?

- `OneTimeWorkRequestBuilder` 
- `PeriodicWorkRequestBuilder`
- `TestWorkerBuilder`
- `TestListenableWorkerBuilder` ✅

#### 10. Lors du test des mises en œuvre de workers, vous pouvez les appeler directement avec `doWork()` au lieu de les ajouter à la file d'attente.

- Vrai ✅
- Faux

## Module 8 : Vues et Compose

### Vues Android et Compose dans les vues

#### 1. Quelle langue est utilisée pour créer les mises en page de type "View" ?

- HTML
- Kotlin
- XML ✅
- Java

#### 2. Lors de la création d'une application avec des vues, par lequel des éléments suivants doit être remplacé le concept de composable "écran" ?

- Fragment ✅
- ViewModel
- Composable
- Activité

#### 3. Les liaisons de vue permettent d'accéder aux éléments `View` déclarés au format XML et d'interagir avec eux.

- Vrai ✅
- Faux

#### 4. Dans quelle méthode de cycle de vie `Fragment` la liaison des vues est-elle gonflée ?

- `onViewCreated()`
- `onCreateView()` ✅
- `onStart()`
- `onResume()`

#### 5. Les composants de la vue sont accessibles avant le gonflement de la liaison des vues.

- Vrai
- Faux ✅

#### 6. Un élément `ComposeView` est un(e) :

- Vue pouvant héberger une vue Android dans une interface utilisateur Compose.
- Vue Android pouvant héberger le contenu de l'interface utilisateur de Jetpack Compose dans une mise en page de type View ✅
- Vue Android pouvant héberger une vue Android dans une mise en page de type View.
- Vue pouvant héberger l'interface utilisateur de Compose dans une interface utilisateur Compose.

#### 7. Jetpack Compose et le système View peuvent coexister dans votre codebase.

- Vrai ✅
- Faux

#### 8. `ComposeView` utilise sa méthode ___ pour afficher les éléments Compose à l'écran.

- `Composable()`
- `setContent()` ✅
- `setComposeContent()`
- `displayComposable()`

#### 9. L'interopérabilité avec les vues a été conçue dès le départ dans Jetpack Compose.

- Vrai ✅
- Faux

#### 10. L'indicateur qui permet à Android Studio de fonctionner avec Compose est le suivant :

- Au niveau du projet, utilisez `buildFeatures { compose true }`
- Au niveau de l'application, utilisez `buildFeatures { compose true }` ✅
- Au niveau du projet, utilisez `buildFeatures { enableCompose true }`
- Au niveau de l'application, utilisez `buildFeatures { enableCompose true }`

### Vues dans Compose

#### 1. Quel composable permet d'implémenter l'interopérabilité d'une vue ?

- `InputRow`
- `Column`
- `TextInputRow`
- `AndroidView` ✅

#### 2. Qu'est-ce qu'un élément `AndroidView` ?

- Un composable qui héberge un élément ou une hiérarchie de type View ✅
- Une vue Android qui héberge le contenu de l'UI Jetpack Compose dans une mise en page de type View
- Une vue Android qui héberge une vue Android dans une mise en page de type View
- Une vue Compose qui héberge le contenu de l'UI Jetpack Compose dans une interface utilisateur Compose

#### 3. Parmi les éléments suivants, lesquels sont des paramètres du composable `AndroidView` ? Plusieurs réponses possibles.
*Choisissez autant de réponses que vous jugez nécessaires.*

- `factory` ✅
- `inputLabel`
- `update` ✅
- `modifier` ✅

#### 4. Le rappel `update` du composable `AndroidView` est appelé une fois que la vue correspondante a été gonflée.

- Vrai ✅
- Faux

#### 5. Quelle est la fonction du lambda `factory` du composable `AndroidView` ?

- Décore et améliore le composable AndroidView
- Exécute le code après le gonflement de la vue
- Crée la vue ✅
