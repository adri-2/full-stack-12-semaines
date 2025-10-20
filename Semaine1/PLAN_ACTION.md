# 🎯 PLAN D'ACTION - CRÉATION DE VOTRE API

## 📅 PLANNING SUR 5 JOURS

---

## 🗓️ JOUR 1 : CONFIGURATION ET MODÈLES SIMPLES

### Matin (2-3h)

- [x] ✅ Lire le GUIDE_API_EXERCISES.md
- [x] Installer les dépendances : `pip install -r requirements_API.txt`
- [x] Configurer DRF dans settings.py (voir CONFIGURATION_DRF.py)
- [x] Faire les migrations : `python manage.py migrate`
- [x] Créer un superuser : `python manage.py createsuperuser`
- [x] Tester que le serveur démarre : `python manage.py runserver`

### Après-midi (3-4h)

**EXERCICE 1 : Category (RÉVISION)**

- [x] Étudier CategoryCreateSerializer, CategoryListSerializer, CategoryDetailSerializer
- [x] Étudier CategoryViewSet
- [x] Tester les endpoints dans le navigateur : http://localhost:8000/api/categories/
- [x] Créer/Modifier/Supprimer des catégories via l'API

**EXERCICE 2 : Supplier**

- [x] ✍️ Compléter SupplierCreateSerializer
- [x] ✍️ Compléter SupplierListSerializer
- [x] ✍️ Compléter SupplierDetailSerializer
- [x] ✍️ Compléter SupplierViewSet
- [x] 🔗 Enregistrer dans urls_EXERCICES.py
- [x] 🧪 Tester : http://localhost:8000/api/suppliers/

**EXERCICE 3 : Client**

- [ ] ✍️ Compléter ClientCreateSerializer
- [ ] ✍️ Compléter ClientListSerializer
- [ ] ✍️ Compléter ClientDetailSerializer
- [ ] ✍️ Compléter ClientViewSet
- [ ] 🔗 Enregistrer dans urls_EXERCICES.py
- [ ] 🧪 Tester : http://localhost:8000/api/clients/

---

## 🗓️ JOUR 2 : MODÈLES AVEC RELATIONS

### Matin (3-4h)

**EXERCICE 4 : Product (LE PLUS IMPORTANT)**

- [ ] ✍️ Compléter ProductCreateSerializer
  - [ ] Validation du prix (> 0)
  - [ ] Validation du stock (>= 0)
  - [ ] Gérer category (ForeignKey)
  - [ ] Gérer suppliers (ManyToMany)
- [ ] ✍️ Compléter ProductListSerializer
  - [ ] Afficher category_name
  - [ ] Ajouter in_stock (boolean)
- [ ] ✍️ Compléter ProductDetailSerializer
  - [ ] Inclure détails de category
  - [ ] Inclure liste des suppliers
  - [ ] Calculer average_rating
  - [ ] Compter reviews_count

### Après-midi (3-4h)

- [ ] ✍️ Compléter ProductViewSet
  - [ ] get_serializer_class()
  - [ ] get_queryset() avec select_related et prefetch_related
  - [ ] Filtres et recherche
- [ ] ✍️ Action personnalisée : low_stock
- [ ] ✍️ Action personnalisée : by_category
- [ ] ✍️ Action personnalisée : reviews
- [ ] 🔗 Enregistrer dans urls_EXERCICES.py
- [ ] 🧪 Tester tous les endpoints

**Auto-évaluation :**

- Créer 3 catégories
- Créer 2 fournisseurs
- Créer 5 produits avec différentes catégories et fournisseurs
- Tester la recherche
- Tester le filtrage

---

## 🗓️ JOUR 3 : AVIS ET REVIEWS

### Matin (2-3h)

**EXERCICE 5 : Review**

- [ ] ✍️ Compléter ReviewCreateSerializer
  - [ ] Validation : rating entre 1 et 5
  - [ ] Validation : comment min 10 caractères
- [ ] ✍️ Compléter ReviewListSerializer
  - [ ] Afficher product_name
  - [ ] Afficher username
- [ ] ✍️ Compléter ReviewDetailSerializer
- [ ] ✍️ Compléter ReviewViewSet
  - [ ] perform_create() pour associer l'utilisateur
- [ ] ✍️ Action personnalisée : top_rated
- [ ] 🔗 Enregistrer dans urls_EXERCICES.py
- [ ] 🧪 Tester

### Après-midi (2-3h)

- [ ] Créer plusieurs avis pour vos produits
- [ ] Vérifier que average_rating fonctionne dans ProductDetailSerializer
- [ ] Tester l'action reviews d'un produit
- [ ] Tester l'action top_rated

**BONUS :**

- [ ] Empêcher un utilisateur de laisser 2 avis sur le même produit
- [ ] Ajouter une action pour obtenir les derniers avis

---

## 🗓️ JOUR 4 : COMMANDES (NIVEAU AVANCÉ)

### Matin (3-4h)

**EXERCICE 6 : Order**

- [ ] ✍️ Compléter OrderCreateSerializer
- [ ] ✍️ Compléter OrderListSerializer
  - [ ] Calculer total_amount
  - [ ] Compter items_count
- [ ] ✍️ Compléter OrderDetailSerializer
  - [ ] Inclure détails du client
  - [ ] Inclure liste des items
- [ ] ✍️ Compléter OrderViewSet
  - [ ] Optimisations avec select_related et prefetch_related
  - [ ] perform_create() pour associer l'utilisateur

### Après-midi (3-4h)

**Actions personnalisées Order :**

- [ ] ✍️ Action confirm : Confirmer une commande
- [ ] ✍️ Action cancel : Annuler une commande
- [ ] ✍️ Action my_orders : Mes commandes
- [ ] ✍️ Action add_item : Ajouter un produit
- [ ] 🔗 Enregistrer dans urls_EXERCICES.py
- [ ] 🧪 Tester toutes les actions

**Test complet :**

- Créer une commande
- Ajouter des articles
- Confirmer la commande
- Tester my_orders

---

## 🗓️ JOUR 5 : ORDERITEMS ET TESTS

### Matin (2-3h)

**EXERCICE 7 : OrderItem**

- [ ] ✍️ Compléter OrderItemCreateSerializer
  - [ ] Validation : quantity > 0
  - [ ] Validation : stock suffisant
- [ ] ✍️ Compléter OrderItemListSerializer
  - [ ] Calculer subtotal
- [ ] ✍️ Compléter OrderItemDetailSerializer
- [ ] ✍️ Compléter OrderItemViewSet
  - [ ] perform_create() pour vérifier le stock
- [ ] 🔗 Enregistrer dans urls_EXERCICES.py
- [ ] 🧪 Tester

### Après-midi (3-4h)

**EXERCICE 8 : Tests unitaires**

- [ ] Lire tests_EXERCICES.py
- [ ] Écrire les tests pour Product
- [ ] Écrire les tests pour Order
- [ ] Écrire les tests pour OrderItem
- [ ] Écrire les tests pour Review
- [ ] Lancer tous les tests : `python manage.py test`
- [ ] Viser 80%+ de couverture de code

**Commandes :**

```bash
# Installer coverage
pip install coverage

# Lancer les tests avec coverage
coverage run --source='.' manage.py test

# Voir le rapport
coverage report

# Générer un rapport HTML
coverage html
# Ouvrir htmlcov/index.html
```

---

## ✅ VALIDATION FINALE

### Checklist complète

- [ ] Tous les serializers sont créés (21 au total)
- [ ] Tous les ViewSets sont créés (7 au total)
- [ ] Toutes les actions personnalisées sont créées (10 au total)
- [ ] Tous les endpoints sont enregistrés dans urls.py
- [ ] La documentation Swagger fonctionne : http://localhost:8000/swagger/
- [ ] Tous les tests passent : `python manage.py test`
- [ ] Couverture de code > 80%

### Test manuel complet (30 min)

1. **Créer des données :**

   - 3 catégories
   - 3 fournisseurs
   - 3 clients
   - 10 produits
   - 5 avis
   - 2 commandes avec plusieurs articles

2. **Tester tous les endpoints :**

   - Liste, création, détail, modification, suppression
   - Recherche et filtrage
   - Actions personnalisées

3. **Tester les validations :**

   - Prix négatif → rejeté
   - Rating hors limites → rejeté
   - Stock insuffisant → rejeté

4. **Tester les relations :**
   - Un produit a une catégorie
   - Un produit a plusieurs fournisseurs
   - Une commande a plusieurs articles
   - Un produit a plusieurs avis

---

## 🎓 CRITÈRES D'ÉVALUATION

| Critère                          | Poids | Votre score |
| -------------------------------- | ----- | ----------- |
| **Serializers complets**         | 25%   | /25         |
| - 3 serializers par modèle       |       |             |
| - Validations correctes          |       |             |
| - Relations bien gérées          |       |             |
| **ViewSets fonctionnels**        | 25%   | /25         |
| - CRUD complet                   |       |             |
| - Optimisations (select_related) |       |             |
| - Filtres et recherche           |       |             |
| **Actions personnalisées**       | 15%   | /15         |
| - 10 actions créées              |       |             |
| - Logique métier correcte        |       |             |
| **URLs et routing**              | 10%   | /10         |
| - Structure cohérente            |       |             |
| - Documentation Swagger          |       |             |
| **Tests unitaires**              | 15%   | /15         |
| - 25+ tests créés                |       |             |
| - Couverture > 80%               |       |             |
| **Qualité du code**              | 10%   | /10         |
| - Code propre                    |       |             |
| - Commentaires                   |       |             |
| - Respect des conventions        |       |             |
| **TOTAL**                        | 100%  | **/100**    |

---

## 🏆 OBJECTIFS DE COMPÉTENCES

À la fin de cet exercice, vous saurez :

### Niveau 1 : Débutant ✅

- [x] Créer des serializers simples
- [x] Utiliser ModelViewSet
- [x] Configurer les URLs avec Router
- [x] Tester l'API avec le navigable API

### Niveau 2 : Intermédiaire ✅

- [ ] Gérer les relations (ForeignKey, ManyToMany)
- [ ] Créer des validations personnalisées
- [ ] Utiliser SerializerMethodField
- [ ] Optimiser les requêtes (select_related, prefetch_related)
- [ ] Filtrer et rechercher
- [ ] Créer des actions personnalisées (@action)

### Niveau 3 : Avancé ✅

- [ ] Gérer les permissions
- [ ] Utiliser get_serializer_class() dynamiquement
- [ ] Surcharger perform_create/perform_update
- [ ] Écrire des tests unitaires complets
- [ ] Calculer des champs (totaux, moyennes)
- [ ] Gérer les erreurs proprement
- [ ] Documenter l'API avec Swagger

### Niveau 4 : Expert 🔥

- [ ] Implémenter un système de pagination personnalisé
- [ ] Créer des permissions personnalisées
- [ ] Ajouter du throttling (limitation de taux)
- [ ] Mettre en cache les résultats
- [ ] Ajouter de la validation cross-field complexe
- [ ] Implémenter des transactions atomiques

---

## 📚 RESSOURCES SUPPLÉMENTAIRES

### Documentation officielle

- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Documentation](https://docs.djangoproject.com/)
- [drf-yasg (Swagger)](https://drf-yasg.readthedocs.io/)

### Tutoriels

- [DRF Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
- [DRF Tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/)

### Outils

- [Postman](https://www.postman.com/) - Tester les APIs
- [HTTPie](https://httpie.io/) - Client HTTP en ligne de commande
- [DB Browser for SQLite](https://sqlitebrowser.org/) - Explorer votre base de données

---

## 💪 MOTIVATION

> "La meilleure façon d'apprendre est de faire."

Vous allez créer **40+ endpoints** fonctionnels !
C'est un projet complet qui peut servir de portfolio.

**Bon courage ! 🚀**

Si vous rencontrez des difficultés :

1. Relisez les exemples (Category est votre référence)
2. Consultez la documentation DRF
3. Testez au fur et à mesure
4. N'hésitez pas à demander de l'aide

**Remember:** Chaque développeur senior que vous admirez a commencé comme vous ! 💪
