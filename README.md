# teoria_sterowania_projekt


Celem robota jest poruszanie się po hali, zbieranie przedmiotów i później odkładanie ich w wyznaczonym miejscu. Rozplanowanie zadań przedstawiono na schemacie poniżej. 


Schemat automatu nadrzędnego          | Automat "is arm over box"
:-------------------------:|:-------------------------:
![](docs/schemat.png)  |  ![](docs/arm_box)
Automat "camera"          | Automat "checking box pos"
![](docs/camera2)  |  ![](docs/check_base_pose)
Automat "grab obj"        | Automat "move arm"
![](docs/grab_obj)  |  ![](docs/move_arm.png)
Automat "move base"         |  Automat "put obj"
![](docs/move_base.png)  |  ![](docs/open_gripper)


Domyślnie robot czeka na przesłanie mu koordynatów xy obiektu do zabrania. Okresla to stan "wait for xy". W momencie odebrania koordytantów sprawdzane jest, czy obiekt znajduje się w zasięgu bazy robota. Jeżeli tak, to następuje wydarzenie A ("base is near"), jeżeli nie to wydarzenie B ("base is not near"). W przypadku wydarzenia B następuje przejście do stanu "move base", który oblicza a następnie porusza się do przestrzeni, w kótrej obiekt będzie w zasięgu bazy (wydarzenie C - "move was done").  Przejście z "wait for xy" poprzez wydarzenie A albo z "move base" przez wydarzenie C prowadzi do stanu "cam". Następuje wtedy sprawdzenie, czy obiekt jest w zasięgu ramienia (na podstawie kamery). Jeżeli nie jest następuje wydarzenie D (arm in not near) i przejście do stanu "move arm", skąd po wykonaniu ruchu ramienia tak, aby mozna było złapać obiekt, następuje wydarzenie F (arm move was done) i powrót do stanu, gdzie kamera sprawdza, czy jesteśmy wstanie chwycić obiekt. Gdy ramie znajduje się w odpowiedniej pozycji, nastepuje poprzez wydarzenie E ("arm is near") przejście do stanu Grab Obj. Z tego stanu, poprzez wydarzenie G "obj was grabbed" przejście do stanu "checking box pos". Następuje sprawdzenie, gdzie znajduje się docelowe miejsce na odłożenie przedmiotu. Jeżeli punkt docelowy znajduje się poza zasięgiem bazy, nastepuje ponownie wydarzenie B ("base is not near"), które prowadzi do stanu Move base, gdzie po wykonaniu ruchu następuje wydarzenie C "move was done" i przejście do wydarzenia "is arm over box". 
Jeżeli w wydarzeniu "Checking box pos" jednak baza będzie w odpowiedniej odległości od miejsca docelowego, wtedy następuje przejście do stanu "is arm over box" poprzez wydarzenie A (base is near). W stanie "is arm over box" wykonywane jest sprawdzenie, czy ramie jest w odpowiednim miejscu, aby odłożyć obiekt, jeżeli nie, poprzez wydarzenie D ("arm is not near") nastepuje przejście do stanu Move arm, skąd po wykonaniu ruchu następuje przejście spowrotem do stanu "is arm over box" poprzez wydarzenie F ("arm move was done"). W momencie, gdy ramie jest w odpowiedniej pozycji, aby odłożyć obiekt, nastepuje przejście ze stanu "is arm over box" do stanu "put obj" przez wydarzenie E ("arm is near"). Nastepnie obiekt zostaje odłożony i poprzez wydarzenie H ("obj was put") nastepuje powrót do domyślnej pętli ("wait for xy").


Interface:
program przyjmuje 3 opcjonalne argumenty: display_trace, path, trace.
Uruchomienie programu bez ich podania sprawi, że uruchomi się domyślna ściezka 0.

Argument path określa, którą ścieżke chcemy uruchomić: 0, 1, albo 2

Argument display_trace wyświetla grafy dla poszczególnych automatów podrzędnych (slaveów). Ważne: podanie tego argumentu sprawi, że wyświetlą się ścieżki, natomiast sam automat się nie uruchomi. Dostępne argumenty: cam, grab, check_box_pos, is_arm, move_a (move arm), move_b (move base), put_o, all. 

Argument trace: wypisuje ścieżki pomiędzy 2 nodami. Szablon podawania nodów: --trace=nodeA.nodeB. Dostępne nody: cam, grab, check_box_pos, is_arm, move_a (move arm), move_b (move base), put_o.
