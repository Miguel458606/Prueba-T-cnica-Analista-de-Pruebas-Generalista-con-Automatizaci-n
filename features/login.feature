
Feature: Proceso de contratación en OrangeHRM

  Scenario: Contratar un nuevo candidato
    Given el usuario accede al sistema con credenciales válidas
    When el usuario navega a la funcionalidad "Recruitment"
    And agrega un candidato con información válida
    Then el candidato aparece en la lista con estado "Hired"
