from get_bearer import *

def list_plan():
    # URL de l'API PayPal
    url = f"{url_add}/v1/billing/plans?sort_by=create_time&sort_order=desc"

    # Jeton d'accès (remplace 'your_access_token_here' par ton véritable jeton d'accès)
    access_token = get_bearer()
    # En-têtes de la requête
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Prefer': 'return=representation'
    }
    # Envoi de la requête GET
    response = requests.get(url, headers=headers)
    # Affichage du statut de la réponse et du contenu
    return (response.json()['plans'])       # Corps de la réponse en JSON



def create_plan(product_id, name, description, status, billing_cycles, payment_preferences, taxes):
    """
    Crée un plan de facturation PayPal.

    :param product_id: ID du produit associé au plan
    :param name: Nom du plan
    :param description: Description du plan
    :param status: Statut du plan (e.g., "ACTIVE")
    :param billing_cycles: Liste des cycles de facturation
    :param payment_preferences: Préférences de paiement
    :param taxes: Taxes associées au plan
    :return: Réponse de l'API PayPal
    """
    # URL de l'API PayPal
    url = f"{url_add}/v1/billing/plans"

    # Jeton d'accès
    access_token = get_bearer()

    # En-têtes de la requête
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Prefer': 'return=representation',
    }

    # Corps de la requête
    data = {
        "product_id": product_id,
        "name": name,
        "description": description,
        "status": status,
        "billing_cycles": billing_cycles,
        "payment_preferences": payment_preferences,
        "taxes": taxes
    }

    # Envoi de la requête POST
    response = requests.post(url, headers=headers, json=data)
    # Retourner la réponse de l'API
    return response.json()

def create_product(name, description, image_url):
    """
    Crée un produit PayPal.

    :param name: Nom du produit
    :param description: Description du produit
    :param product_type: Type du produit (e.g., "SERVICE")
    :param category: Catégorie du produit (e.g., "SOFTWARE")
    :param image_url: URL de l'image du produit
    :param home_url: URL de la page d'accueil du produit
    :return: Réponse de l'API PayPal
    """
    # URL de l'API PayPal
    url = f"{url_add}/v1/catalogs/products"

    # Jeton d'accès
    access_token = get_bearer()

    # En-têtes de la requête
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Prefer': 'return=representation',
    }

    # Corps de la requête
    data = {
        "name": name,
        "description": description,
        "type": "SERVICE",
        "category": "PHOTOGRAPHY",
        "image_url": image_url,
        "home_url": os.environ.get('PUBLIC_TELEGRAM_LINK')
    }

    # Envoi de la requête POST
    response = requests.post(url, headers=headers, json=data)

    # Retourner la réponse de l'API
    return response.json()



def list_product(page_size=2, page=1):
    """
    Liste les produits disponibles dans le catalogue PayPal.

    :param page_size: Nombre de produits par page
    :param page: Numéro de la page à récupérer
    :return: Réponse de l'API PayPal
    """
    # URL de l'API PayPal
    url = f"{url_add}/v1/catalogs/products"

    # Jeton d'accès
    access_token = get_bearer()

    # En-têtes de la requête
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    # Paramètres de la requête
    params = {
        'page_size': page_size,
        'page': page,
        'total_required': 'true'
    }

    # Envoi de la requête GET
    response = requests.get(url, headers=headers, params=params)

    # Retourner la réponse de l'API
    return response.json()
