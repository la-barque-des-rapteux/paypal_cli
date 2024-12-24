from plans import *


def main():
    while True:
        print("\n--- Gestion de PayPal ---")
        print("1. Créer un produit")
        print("2. Lister les plans")
        print("3. Créer un plan")
        print("4. Lister les produits")
        print("5. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            print("\n--- Création d'un produit ---")
            name = input("Nom du produit : ")
            description = input("Description du produit : ")
            image_url = input("URL de l'image du produit : ")
            response = create_product(name, description, image_url)
            print("\nRéponse :", response)

        elif choice == "2":
            print("\n--- Liste des plans ---")
            response = list_plan()
            print("\nPlans disponibles :")
            for plan in response:
                print(f"- {plan['name']} (ID: {plan['id']})")

        elif choice == "3":
            print("\n--- Création d'un plan ---")
            product_id = input("ID du produit : ")
            name = input("Nom du plan : ")
            description = input("Description du plan : ")
            status = input("Statut du plan (e.g., ACTIVE) : ")

            billing_cycles = []
            print("\nAjout des cycles de facturation (laisser vide pour arrêter) :")
            while True:
                interval_unit = input("Unité d'intervalle (e.g., MONTH) : ")
                if not interval_unit:
                    break
                interval_count = int(input("Nombre d'intervalles : "))
                tenure_type = input("Type de durée (e.g., TRIAL, REGULAR) : ")
                sequence = int(input("Séquence : "))
                total_cycles = int(input("Nombre total de cycles : "))
                fixed_price = input("Prix fixe (e.g., 10) : ")
                currency_code = input("Code de la monnaie (e.g., USD) : ")

                billing_cycles.append({
                    "frequency": {
                        "interval_unit": interval_unit,
                        "interval_count": interval_count
                    },
                    "tenure_type": tenure_type,
                    "sequence": sequence,
                    "total_cycles": total_cycles,
                    "pricing_scheme": {
                        "fixed_price": {
                            "value": fixed_price,
                            "currency_code": currency_code
                        }
                    }
                })

            payment_preferences = {
                "auto_bill_outstanding": True,
                "setup_fee": {
                    "value": input("Frais d'installation (e.g., 10) : "),
                    "currency_code": input("Code de la monnaie pour les frais d'installation (e.g., USD) : ")
                },
                "setup_fee_failure_action": "CONTINUE",
                "payment_failure_threshold": int(input("Seuil d'échec de paiement : "))
            }

            taxes = {
                "percentage": input("Pourcentage de taxe (e.g., 10) : "),
                "inclusive": input("Taxes incluses ? (True/False) : ").lower() == "true"
            }

            response = create_plan(product_id, name, description, status, billing_cycles, payment_preferences, taxes)
            print("\nRéponse :", response)

        elif choice == "4":
            print("\n--- Liste des produits ---")
            page_size = int(input("Nombre de produits par page : "))
            page = int(input("Numéro de la page : "))
            response = list_product(page_size=page_size, page=page)
            print("\nProduits disponibles :")
            for product in response.get('products', []):
                print(f"- {product['name']} (ID: {product['id']})")

        elif choice == "5":
            print("\nAu revoir !")
            break

        else:
            print("\nOption invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
