
from typing import List, Dict, Any, Optional
from my_project.auth.service.orders import actor_service
from my_project.auth.controller.general_controller import GeneralController



class ActorController(GeneralController):
    _service = actor_service  
    
    def get_movies_by_actor_id_route(self, actor_id: int) -> List[Dict[str, Any]]:
        movies_data = self._service.find_movies_by_actor_id(actor_id)
        return list(map(lambda x: dict(x), movies_data))
        
    def get_actor_by_nationality_route(self, nationality: str) -> List[Dict[str, Any]]:
        actor_nat = self._service.find_by_nationality(nationality)
        return list(map(lambda x: dict(x), actor_nat))
