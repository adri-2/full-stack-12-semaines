# 🚀 COMMENCEZ ICI - FORMATION API DJANGO REST FRAMEWORK

## 👋 Bienvenue !

Vous êtes sur le point d'apprendre à créer une **API REST professionnelle complète** avec Django REST Framework.

---

## 📖 PAR OÙ COMMENCER ?

### 1️⃣ LISEZ D'ABORD (15 minutes)

**Commencez par ce fichier** → **[RECAPITULATIF_FINAL.md](RECAPITULATIF_FINAL.md)**

- Vue d'ensemble complète
- Ce que vous allez apprendre
- Structure des fichiers

### 2️⃣ COMPRENEZ LES CONCEPTS (30 minutes)

**Puis lisez** → **[GUIDE_API_EXERCISES.md](GUIDE_API_EXERCISES.md)**

- Concepts théoriques
- Types de serializers
- Types de vues
- Bonnes pratiques

### 3️⃣ PLANIFIEZ VOTRE TRAVAIL (10 minutes)

**Consultez** → **[PLAN_ACTION.md](PLAN_ACTION.md)**

- Planning sur 5 jours
- Objectifs quotidiens
- Auto-évaluation

---

## 🛠️ INSTALLATION (30 minutes)

### Étape 1 : Activer l'environnement

```powershell
cd "c:\Users\wwwad\PycharmProjects\FULL STACK DEV"
venv\Scripts\activate
```

### Étape 2 : Installer les dépendances

```powershell
cd Semaine1\testmodels
pip install -r requirements_API.txt
```

### Étape 3 : Configurer Django

Ouvrez `testmodels/settings.py` et copiez la configuration de **[CONFIGURATION_DRF.py](testmodels/CONFIGURATION_DRF.py)**

### Étape 4 : Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Étape 5 : Créer un superuser

```powershell
python manage.py createsuperuser
```

### Étape 6 : Lancer le serveur

```powershell
python manage.py runserver
```

### Étape 7 : Vérifier que ça marche

Ouvrez votre navigateur :

- http://localhost:8000/admin/ (se connecter avec le superuser)

---

## ✍️ COMMENCEZ À CODER

### JOUR 1 : Modèles simples (4-6h)

#### Matin : Étude de l'exemple

1. Ouvrez **[serializers_EXERCICES.py](testmodels/app/serializers_EXERCICES.py)**
2. Étudiez les 3 serializers de Category (lignes 1-100)
3. Ouvrez **[views_EXERCICES.py](testmodels/app/views_EXERCICES.py)**
4. Étudiez CategoryViewSet (lignes 1-150)
5. Testez : http://localhost:8000/api/categories/

#### Après-midi : Supplier

1. Dans **serializers_EXERCICES.py**, complétez :
   - SupplierCreateSerializer
   - SupplierListSerializer
   - SupplierDetailSerializer
2. Dans **views_EXERCICES.py**, complétez :
   - SupplierViewSet
3. Dans **urls_EXERCICES.py**, enregistrez le ViewSet
4. Testez : http://localhost:8000/api/suppliers/

#### Soir : Client

Répétez le processus pour Client

---

### JOUR 2 : Product (4-5h)

Le plus important ! Product a des relations complexes.

1. Complétez ProductCreateSerializer
   - Validation du prix
   - Validation du stock
   - Gérer category (ForeignKey)
   - Gérer suppliers (ManyToMany)
2. Complétez ProductListSerializer
3. Complétez ProductDetailSerializer
4. Complétez ProductViewSet
5. Créez les 3 actions personnalisées
6. Testez exhaustivement

---

### JOUR 3-5 : Continuez selon le plan

Suivez **[PLAN_ACTION.md](PLAN_ACTION.md)** pour les jours suivants.

---

## 📚 FICHIERS DE RÉFÉRENCE

### 📝 Guides et documentation

- **[RECAPITULATIF_FINAL.md](RECAPITULATIF_FINAL.md)** - Vue d'ensemble complète
- **[GUIDE_API_EXERCISES.md](GUIDE_API_EXERCISES.md)** - Guide pédagogique
- **[PLAN_ACTION.md](PLAN_ACTION.md)** - Planning sur 5 jours
- **[README_EXERCICES.md](README_EXERCICES.md)** - Point d'entrée
- **[AIDE_MEMOIRE.md](AIDE_MEMOIRE.md)** - Commandes utiles

### 💻 Fichiers de code

- **[testmodels/app/serializers_EXERCICES.py](testmodels/app/serializers_EXERCICES.py)** - 18 serializers à créer
- **[testmodels/app/views_EXERCICES.py](testmodels/app/views_EXERCICES.py)** - 7 ViewSets à créer
- **[testmodels/testmodels/urls_EXERCICES.py](testmodels/testmodels/urls_EXERCICES.py)** - Configuration URLs
- **[testmodels/app/tests_EXERCICES.py](testmodels/app/tests_EXERCICES.py)** - 25+ tests à écrire

### ⚙️ Configuration

- **[testmodels/CONFIGURATION_DRF.py](testmodels/CONFIGURATION_DRF.py)** - Config DRF à copier
- **[testmodels/requirements_API.txt](testmodels/requirements_API.txt)** - Dépendances

---

## 🎯 OBJECTIFS

À la fin, vous aurez :

- ✅ 40+ endpoints RESTful
- ✅ 21 serializers complets
- ✅ 7 ViewSets fonctionnels
- ✅ 10 actions personnalisées
- ✅ 25+ tests unitaires
- ✅ Documentation Swagger automatique
- ✅ Une API complète et professionnelle

---

## 💡 CONSEILS

1. **Ne sautez pas d'étapes** - Category est votre référence
2. **Testez immédiatement** - Après chaque modification
3. **Utilisez le browsable API** - http://localhost:8000/api/
4. **Lisez les TODO** - Chaque fichier a des instructions détaillées
5. **Consultez AIDE_MEMOIRE.md** - Pour les commandes et exemples

---

## 🆘 BESOIN D'AIDE ?

### Si le serveur ne démarre pas

```powershell
python manage.py check
```

### Si vous êtes bloqué sur un serializer

Regardez l'exemple de Category (déjà fait)

### Si vous ne comprenez pas un concept

Lisez **[GUIDE_API_EXERCISES.md](GUIDE_API_EXERCISES.md)**

### Si vous ne savez pas par où commencer

Suivez **[PLAN_ACTION.md](PLAN_ACTION.md)** jour par jour

---

## 🧪 TESTER VOTRE PROGRESSION

### Après chaque modèle

- [ ] Les 3 serializers créés
- [ ] Le ViewSet créé
- [ ] Enregistré dans urls.py
- [ ] Testé dans le navigateur
- [ ] Actions personnalisées créées (si applicable)

### Commandes de test

```powershell
# Lancer le serveur
python manage.py runserver

# Tester dans le navigateur
# http://localhost:8000/api/categories/
# http://localhost:8000/api/suppliers/
# http://localhost:8000/api/clients/
# etc.

# Documentation Swagger
# http://localhost:8000/swagger/
```

---

## 📊 PROGRESSION

```
JOUR 1 : Configuration + Supplier + Client
  ⬜ Installation et configuration
  ⬜ Supplier (3 serializers + ViewSet)
  ⬜ Client (3 serializers + ViewSet)

JOUR 2 : Product
  ⬜ Product (3 serializers + ViewSet + 3 actions)

JOUR 3 : Review
  ⬜ Review (3 serializers + ViewSet + 1 action)

JOUR 4 : Order
  ⬜ Order (3 serializers + ViewSet + 4 actions)

JOUR 5 : OrderItem + Tests
  ⬜ OrderItem (3 serializers + ViewSet)
  ⬜ Tests unitaires (25+)
```

---

## 🎉 FÉLICITATIONS !

Vous avez maintenant tout ce qu'il faut pour réussir !

**Temps estimé : 13-17 heures**
**Résultat : Une API professionnelle complète**

---

## 🚀 PRÊT ? C'EST PARTI !

### Étape suivante :

1. Lisez **[RECAPITULATIF_FINAL.md](RECAPITULATIF_FINAL.md)**
2. Installez les dépendances
3. Ouvrez **[serializers_EXERCICES.py](testmodels/app/serializers_EXERCICES.py)**
4. Commencez à coder !

**Bon courage ! 💪**

---

> "Le meilleur moment pour planter un arbre était il y a 20 ans. Le deuxième meilleur moment est maintenant." - Proverbe chinois

**Commencez maintenant ! Vous pouvez le faire ! 🚀**
