def mtf(config_list, request_sequence, details=False):
    """
    Implementación del algoritmo Move to Front (MTF)
    
    Args:
        config_list (list): Lista de configuración inicial
        request_sequence (list): Secuencia de solicitudes
        details (bool): Si True, imprime detalles de cada paso
        
    Returns:
        tuple: (costo_total, config_list_final)
    """
    cost = 0
    current_config = config_list.copy()
    
    if details:
        print("Configuración inicial:", current_config)
    
    for request in request_sequence:
        # Encontrar la posición del elemento solicitado
        try:
            pos = current_config.index(request)
        except ValueError:
            raise ValueError(f"Elemento {request} no encontrado en la lista de configuración")
        
        # El costo es la posición + 1 (ya que empieza en 0)
        request_cost = pos + 1
        cost += request_cost
        
        # Mover el elemento al frente
        if pos != 0:
            current_config.pop(pos)
            current_config.insert(0, request)
        
        if details:
            print(f"Solicitud: {request}, Costo: {request_cost}, Configuración: {current_config}")
    
    if details:
        print("Costo total de acceso:", cost)
    
    return cost, current_config