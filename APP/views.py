from django.http import HttpResponse
from django.template import *
from django.shortcuts import *

# Estos metodos hacen referencia a las paginas creadas.
# Agrega aqui tu pagina declarando un metodo

def index(request):
    return HttpResponse('<h1 style="text-align:center;">Pagina inicio</h1>')

def inicio(request):
    return render(request,'inicio.html')

def registrarse(request):
    return HttpResponse('''<section class="vh-100" style="background-color: #eee;">
  <div class="container h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-lg-12 col-xl-11">
        <div class="card text-black" style="border-radius: 25px;">
          <div class="card-body p-md-5">
            <div class="row justify-content-center">
              <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">

                <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Registrate</p>

                <form class="mx-1 mx-md-4">

                  <div class="d-flex flex-row align-items-center mb-4">
                    <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                    <div class="form-outline flex-fill mb-0">
                      <label class="form-label" for="form3Example1c">Nombres:</label>
                      <input type="text" id="form3Example1c" class="form-control" />
                      
                    
                    </div>

                    <br></br>

                     <div class="form-outline flex-fill mb-0">
                      <label class="form-label" for="form3Example1c">Apellidos:</label>
                      <input type="text" id="form3Example1c" class="form-control" />
                      
                    
                    </div>
                    <br></br>

                     <div class="form-outline flex-fill mb-0">
                      <label class="form-label" for="form3Example1c">Nacionalidad:</label>
                      <form>
                        <select>
                          <option selected="selected">Salvadoreño</option>
                          <option>extranjero</option>

                        </select>
                      
                      </form>
                    
                    </div>

                    <br></br>

                     <div class="form-outline flex-fill mb-0">
                      <label class="form-label" for="form3Example1c">Fecha de nacimiento:</label>
                      <input type="date" id="start" name="trip-start"
                        value="2022-06-18"
                        min="2022-01-01" max="2026-12-31">
                      
                    
                    </div>

                    <br></br>

                     <div class="form-outline flex-fill mb-0">
                      <label class="form-label" for="form3Example1c">Documento de identidad :</label>
                      <form>
                          <select>

                          <option selected="selected">DUI</option>
                          <option>NIT</option>
                          <option>Permiso de residencia</option>
                          <option>Pasaporte</option>

                          </select>
                       </form><input type="text" id="form3Example1c" class="form-control" size="50" value="Escriba su numero de identidad">
                      
                    
                    </div>

                    <br></br>

                     <div class="form-outline flex-fill mb-0">
                      <label class="form-label" for="form3Example1c">Sexo:</label>
                      <form>

                        <select>

                          <option selected="selected"> - Elija una opcion - </option>
                          <option>Masculino</option>
                          <option>Femenino</option>


                        </select>

                      </form>
                      
                    
                    </div>

                    <br></br>

                     <div class="form-outline flex-fill mb-0">
                      <label class="form-label" for="form3Example1c">Correo electrónico:</label>
                      <input type="text" id="form3Example1c" class="form-control" />
                      
                    
                    </div>
                    
                    <br></br>

                     <div class="form-outline flex-fill mb-0">
                      <label class="form-label" for="form3Example1c">Cree una contraseña:</label>
                      <input type="password" id="form3Example1c" class="form-control" />
                      
                    
                    </div>
                    
                    <br></br>

                     <div class="form-outline flex-fill mb-0">
                      <label class="form-label" for="form3Example1c">Confirme la contraseña:</label>
                      <input type="password" id="form3Example1c" class="form-control" />
                      
                    
                    </div>
                    
                    <br></br>

                     <div class="form-outline flex-fill mb-0">
                      <label class="form-label" for="form3Example1c">Teléfono:</label>
                      <input type="text" id="form3Example1c" class="form-control" />
                      
                    
                    </div>

                    <br></br>

                     <div class="form-outline flex-fill mb-0">
                      <label class="form-label" for="form3Example1c">Pais de residencia:</label>
                      <input type="text" id="form3Example1c" class="form-control" />
                      
                    
                    </div>

                  </div>

                  <br></br>

                  <div class="form-check d-flex justify-content-center mb-5">
                    <input class="form-check-input me-2" type="checkbox" value="" id="form2Example3c" />
                    <label class="form-check-label" for="form2Example3">
                      Acepto <a href="#!">Términos y condiciones</a>
                    </label>
                  </div>

                  <br></br>

                  <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                    <button type="button" class="btn btn-primary btn-lg">Siguiente</button>
                  </div>

                </form>

              </div>
              <div class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">

              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>''')    


def Crear(request):
  return HttpResponse(''' <section class="vh-100" style="background-color: #eee;">
  <div class="container h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-lg-12 col-xl-11">
        <div class="card text-black" style="border-radius: 25px;">
          <div class="card-body p-md-5">
            <div class="row justify-content-center">
              <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">

                <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Crear Reserva</p>

                <label class="form-label" for="form3Example1c">Paquete seleccionado: </label>
                <br></br>
                <label class="form-label" for="form3Example1c">Informacion del usuario</label>
                <br></br>
                <label class="form-label" for="form3Example1c">Nombres:</label>
                <br></br>
                <label class="form-label" for="form3Example1c">Apellido:</label>
                <br></br>
                <label class="form-label" for="form3Example1c">Teléfono: </label>
                <br></br>
                <label class="form-label" for="form3Example1c">Correo electrónico:</label>
                <br></br>
                <label class="form-label" for="form3Example1c">Documento de identidad:</label>
                <br></br>
                <label class="form-label" for="form3Example1c">---------------------------</label>
                <br></br>
                <label class="form-label" for="form3Example1c">Informacion adicional:</label>
                <br></br>
                <legend>Seleccione el método de pago a utilizar:</legend>
                <label>
                  <input type="radio" name="color" value="Efectivo"> Efectivo
                </label>
                <p><label>
                  <input type="radio" name="color" value="Tarjeta de crédito">Tarjeta de crédito
                </label></p>    
                <br></br>

                <label class="form-label" for="form3Example1c">Información bancaria:</label>
                <br></br>
                <label class="form-label" for="form3Example1c">Número de tarjeta:</label>
                <input type="text" id="form3Example1c" class="form-control" />
                <br></br>
                <label class="form-label" for="form3Example1c">Nombre del propietario:</label>
                <input type="text" id="form3Example1c" class="form-control" />
                <br></br>
                <label class="form-label" for="form3Example1c">Fecha de vencimiento:</label>
              
                <input type="date" id="start" name="trip-start"
                        value="2022-06-18"
                        min="2022-01-01" max="2026-12-31">

                <br></br>

                <label class="form-label" for="form3Example1c">Correo electrónico:</label>
                <input type="text" id="form3Example1c" class="form-control" />

                <br></br>

                <label class="form-label" for="form3Example1c">Código de tarjeta:</label>
                <input type="text" id="form3Example1c" class="form-control" />
 </div>

 <br></br>
 
 <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                    <button type="button" class="btn btn-primary btn-lg">Guardar</button>
                  </div>

                  <br></br>
                  
                  <pr><div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                    <button type="button" class="btn btn-primary btn-lg">Cancelar</button>
                  </div> ''')

