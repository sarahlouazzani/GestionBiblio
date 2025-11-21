"""Script pour remplir la base de données avec des données de test"""
from app import create_app, db
from app.models.users import User
from app.models.books import Book
from app.models.loans import Loan
from app.models.reservations import Reservation
from datetime import datetime, timedelta

def seed_database():
    app = create_app()
    with app.app_context():
        print("🌱 Début du remplissage de la base de données...")
        
        # Nettoyer les données existantes (optionnel)
        print("🧹 Nettoyage des anciennes données...")
        Reservation.query.delete()
        Loan.query.delete()
        Book.query.delete()
        User.query.delete()
        db.session.commit()
        
        # Créer des utilisateurs
        print("👥 Création des utilisateurs...")
        users = [
            User(name="Admin Principal", email="admin@biblio.fr", role="admin"),
            User(name="Marie Dupont", email="marie.dupont@email.fr", role="member"),
            User(name="Jean Martin", email="jean.martin@email.fr", role="member"),
            User(name="Sophie Bernard", email="sophie.bernard@email.fr", role="member"),
            User(name="Pierre Dubois", email="pierre.dubois@email.fr", role="member"),
            User(name="Claire Lefebvre", email="claire.lefebvre@email.fr", role="admin"),
        ]
        
        for user in users:
            user.set_password("password123")
            db.session.add(user)
        
        db.session.commit()
        print(f"✅ {len(users)} utilisateurs créés")
        
        # Créer des livres
        print("📚 Création des livres...")
        books = [
            Book(title="Le Petit Prince", author="Antoine de Saint-Exupéry", isbn="978-2070612758", available=True),
            Book(title="1984", author="George Orwell", isbn="978-0451524935", available=True),
            Book(title="L'Étranger", author="Albert Camus", isbn="978-2070360024", available=True),
            Book(title="Harry Potter à l'école des sorciers", author="J.K. Rowling", isbn="978-2070584628", available=False),
            Book(title="Le Seigneur des Anneaux", author="J.R.R. Tolkien", isbn="978-2266154345", available=True),
            Book(title="Les Misérables", author="Victor Hugo", isbn="978-2253096337", available=True),
            Book(title="Germinal", author="Émile Zola", isbn="978-2253004226", available=False),
            Book(title="Le Comte de Monte-Cristo", author="Alexandre Dumas", isbn="978-2253098058", available=True),
            Book(title="Voyage au bout de la nuit", author="Louis-Ferdinand Céline", isbn="978-2070360987", available=True),
            Book(title="L'Alchimiste", author="Paulo Coelho", isbn="978-2290334249", available=True),
            Book(title="Fondation", author="Isaac Asimov", isbn="978-2070415618", available=True),
            Book(title="Dune", author="Frank Herbert", isbn="978-2221116265", available=False),
            Book(title="Le Meilleur des mondes", author="Aldous Huxley", isbn="978-2266283038", available=True),
            Book(title="Fahrenheit 451", author="Ray Bradbury", isbn="978-2070360871", available=True),
            Book(title="Le Nom de la rose", author="Umberto Eco", isbn="978-2253033448", available=True),
            Book(title="Cent ans de solitude", author="Gabriel García Márquez", isbn="978-2020238113", available=True),
            Book(title="Crime et Châtiment", author="Fiodor Dostoïevski", isbn="978-2253098898", available=True),
            Book(title="Guerre et Paix", author="Léon Tolstoï", isbn="978-2253098706", available=True),
            Book(title="Orgueil et Préjugés", author="Jane Austen", isbn="978-2253260639", available=True),
            Book(title="Le Portrait de Dorian Gray", author="Oscar Wilde", isbn="978-2253006350", available=True),
        ]
        
        for book in books:
            db.session.add(book)
        
        db.session.commit()
        print(f"✅ {len(books)} livres créés")
        
        # Créer des emprunts
        print("📖 Création des emprunts...")
        loans = [
            Loan(
                user_id=users[1].id,  # Marie
                book_id=books[3].id,  # Harry Potter
                date_loaned=datetime.now() - timedelta(days=10),
                due_date=datetime.now() + timedelta(days=4),
                returned=False
            ),
            Loan(
                user_id=users[2].id,  # Jean
                book_id=books[6].id,  # Germinal
                date_loaned=datetime.now() - timedelta(days=5),
                due_date=datetime.now() + timedelta(days=9),
                returned=False
            ),
            Loan(
                user_id=users[3].id,  # Sophie
                book_id=books[11].id,  # Dune
                date_loaned=datetime.now() - timedelta(days=20),
                due_date=datetime.now() - timedelta(days=6),  # En retard
                returned=False
            ),
            Loan(
                user_id=users[1].id,  # Marie
                book_id=books[0].id,  # Le Petit Prince
                date_loaned=datetime.now() - timedelta(days=30),
                due_date=datetime.now() - timedelta(days=16),
                returned=True
            ),
            Loan(
                user_id=users[4].id,  # Pierre
                book_id=books[10].id,  # Fondation
                date_loaned=datetime.now() - timedelta(days=25),
                due_date=datetime.now() - timedelta(days=11),
                returned=True
            ),
        ]
        
        for loan in loans:
            db.session.add(loan)
        
        db.session.commit()
        print(f"✅ {len(loans)} emprunts créés")
        
        # Créer des réservations
        print("🔖 Création des réservations...")
        reservations = [
            Reservation(
                user_id=users[2].id,  # Jean
                book_id=books[3].id,  # Harry Potter (emprunté par Marie)
                date_reserved=datetime.now() - timedelta(days=2),
                status="active"
            ),
            Reservation(
                user_id=users[4].id,  # Pierre
                book_id=books[6].id,  # Germinal (emprunté par Jean)
                date_reserved=datetime.now() - timedelta(days=1),
                status="active"
            ),
            Reservation(
                user_id=users[1].id,  # Marie
                book_id=books[11].id,  # Dune (emprunté par Sophie)
                date_reserved=datetime.now() - timedelta(days=3),
                status="active"
            ),
            Reservation(
                user_id=users[3].id,  # Sophie
                book_id=books[4].id,  # Le Seigneur des Anneaux (disponible)
                date_reserved=datetime.now() - timedelta(days=5),
                status="completed"
            ),
        ]
        
        for reservation in reservations:
            db.session.add(reservation)
        
        db.session.commit()
        print(f"✅ {len(reservations)} réservations créées")
        
        print("\n✨ Base de données remplie avec succès!")
        print("\n📊 Récapitulatif:")
        print(f"   - Utilisateurs: {User.query.count()}")
        print(f"   - Livres: {Book.query.count()}")
        print(f"   - Emprunts: {Loan.query.count()}")
        print(f"   - Réservations: {Reservation.query.count()}")
        print("\n🔑 Identifiants de connexion:")
        print("   Email: admin@biblio.fr")
        print("   Mot de passe: password123")
        print("\n   Autres utilisateurs utilisent aussi: password123")

if __name__ == "__main__":
    seed_database()
