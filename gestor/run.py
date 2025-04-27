import sys
try:
    from gestor import ui as gradio_ui
    from . import database as db
    from . import menu
except ImportError:
    # En caso de que la importación relativa falle, se asume que se está
    # ejecutando el script de otra forma.
    import ui as gradio_ui
    import database as db
    import menu

def terminal_check():
    print("Running terminal check...")
    try:
        count = len(db.Clientes.lista_clientes)
        print(f"Database connection successful. Number of clients: {count}")
    except Exception as e:
        print(f"Error during terminal check: {e}")

def main():
    # Asegurarse de cargar la base de datos con la ruta actual.
    db.Clientes.cargar()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "-t":
            terminal_check()
        elif sys.argv[1] == "-m":
            menu.iniciar()
        else:
            print(f"Opción desconocida: {sys.argv[1]}")
    else:
        gradio_ui.launch_ui()

if __name__ == "__main__":
    main()