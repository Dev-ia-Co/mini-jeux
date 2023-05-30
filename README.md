# Mini-Jeux

Ce répertoire contient plusieurs mini-jeux développés en utilisant différents langages de programmation.

## Idées de jeux

Vous trouverez ci-dessous une liste d'idées de jeux que vous pouvez implémenter :

- [x] Chi-fou-mi
- [ ] Allumettes
- [ ] Dames
- [ ] Labyrinthes
- [x] Morpion
- [ ] Pendu
- [ ] Jeux de Cartes : BlackJack, poker, Bataille
- [x] Mastermind
- [ ] Puissance 4


## Docker

Pour faciliter le déploiement et l'exécution des mini-jeux, vous pouvez utiliser Docker. Docker permet de créer des conteneurs isolés qui contiennent tous les éléments nécessaires à l'exécution d'une application.

Pour exécuter les mini-jeux à l'aide de Docker, suivez les étapes suivantes :

1. Assurez-vous d'avoir Docker installé sur votre système.
2. Clonez ce dépôt sur votre machine.
3. Accédez au répertoire du mini-jeu que vous souhaitez exécuter.
4. Construisez l'image Docker en exécutant la commande suivante :
`docker build -t nom_image .`
Remplacez `nom_image` par le nom que vous souhaitez donner à votre image Docker.
`docker run --rm -it nom_image`
5. Une fois l'image construite, vous pouvez exécuter le mini-jeu en utilisant la commande :
Assurez-vous de remplacer `nom_image` par le nom de l'image Docker que vous avez spécifié précédemment.

Vous devriez maintenant voir le mini-jeu s'exécuter dans votre terminal.

N'hésitez pas à consulter la documentation de Docker pour plus d'informations sur son utilisation et ses fonctionnalités.
