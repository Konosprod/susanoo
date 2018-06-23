import urllib3.request
import certifi
import json

class People:

    id = None
    name = None
    gender = None
    age = None
    eye_color = None
    hair_color = None
    films = None
    species = None
    url = None

    def __init__(self, obj = None):
        if(obj is not None):
            self.__dict__ = obj

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4)

class Film:
    
    id = None
    title = None
    description = None
    director = None
    producer = None
    release_date = None
    rt_score = None
    people = None
    species = None
    locations = None
    url = None

    def __init__(self, obj = None):
        if(obj is not None):
            self.__dict__ = obj

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4)

class Location:
    
    id = None
    name = None
    climate = None
    terrain = None
    surface_water = None
    residents = None
    films = None
    url = None

    def __init__(self, obj = None):
        if(obj is not None):
            self.__dict__ = obj

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4)

class Species:
    
    id = None
    name = None
    classification = None
    eye_color = None
    hair_color = None
    people = None
    films = None
    url = None

    def __init__(self, obj = None):
        if(obj is not None):
            self.__dict__ = obj

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4)

class Vehicle:
    
    id = None
    name = None
    description = None
    vehicle_class = None
    length = None
    pilot = None
    films = None
    url = None

    def __init__(self, obj = None):
        if(obj is not None):
            self.__dict__ = obj

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4)

class Susanoo:
    
    _base_url = "https://ghibliapi.herokuapp.com"
    _http = None

    def __init__(self):
        self._http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())

    def films(self, limit = None, fields = None):
        ret = []
        url = self._base_url + "/films?"

        if(limit is not None):
            url += "limit=" + str(limit) + "&"

        if(fields is not None):
            url += "fields=" + ",".join(fields) + "&"


        data = self._http.request("GET", url)

        if(data.status == 200):
            films = json.loads(data.data.decode("utf-8"))

            for film in films:
                ret.append(Film(film))

        return ret

    def film(self, id, fields = None):
        url = self._base_url + "/films/" + id + "?"

        if(fields is not None):
            url += "fields=" + ",".join(fields)

        data = self._http.request("GET", url)

        if(data.status == 200):
            film = Film(json.loads(data.data.decode("utf-8")))

            return film
        else:
            return None

    def people(self, limit = None, fields = None):
        ret = []
        url = self._base_url + "/people?"

        if(limit is not None):
            url += "limit=" + str(limit) + "&"

        if(fields is not None):
            url += "fields=" + ",".join(fields) + "&"


        data = self._http.request("GET", url)

        if(data.status == 200):
            people = json.loads(data.data.decode("utf-8"))

            for p in people:
                ret.append(People(p))

        return ret

    def people2(self, id, fields = None):
        url = self._base_url + "/people/" + id + "?"

        if(fields is not None):
            url += "fields=" + ",".join(fields)

        data = self._http.request("GET", url)

        if(data.status == 200):
            people = People(json.loads(data.data.decode("utf-8")))

            return people
        else:
            return None

    def locations(self, limit = None, fields = None):
        ret = []
        url = self._base_url + "/locations?"

        if(limit is not None):
            url += "limit=" + str(limit) + "&"

        if(fields is not None):
            url += "fields=" + ",".join(fields) + "&"


        data = self._http.request("GET", url)

        if(data.status == 200):
            locations = json.loads(data.data.decode("utf-8"))

            for location in locations:
                ret.append(Location(location))

        return ret

    def location(self, id, fields = None):
        url = self._base_url + "/locations/" + id + "?"

        if(fields is not None):
            url += "fields=" + ",".join(fields)

        data = self._http.request("GET", url)

        if(data.status == 200):
            location = Location(json.loads(data.data.decode("utf-8")))

            return location
        else:
            return None

    def species(self, limit = None, fields = None):
        ret = []
        url = self._base_url + "/species?"

        if(limit is not None):
            url += "limit=" + str(limit) + "&"

        if(fields is not None):
            url += "fields=" + ",".join(fields) + "&"


        data = self._http.request("GET", url)

        if(data.status == 200):
            species = json.loads(data.data.decode("utf-8"))

            for s in species:
                ret.append(Species(s))

        return ret

    def species2(self, id, fields = None):
        url = self._base_url + "/species/" + id + "?"

        if(fields is not None):
            url += "fields=" + ",".join(fields)

        data = self._http.request("GET", url)

        if(data.status == 200):
            species = Species(json.loads(data.data.decode("utf-8")))

            return species
        else:
            return None

    def vehicles(self, limit = None, fields = None):
        ret = []
        url = self._base_url + "/vehicles?"

        if(limit is not None):
            url += "limit=" + str(limit) + "&"

        if(fields is not None):
            url += "fields=" + ",".join(fields) + "&"


        data = self._http.request("GET", url)

        if(data.status == 200):
            vehicles = json.loads(data.data.decode("utf-8"))

            for vehicle in vehicles:
                ret.append(Vehicle(vehicle))

        return ret

    def vehicle(self, id, fields = None):
        url = self._base_url + "/vehicles/" + id + "?"

        if(fields is not None):
            url += "fields=" + ",".join(fields)

        data = self._http.request("GET", url)

        if(data.status == 200):
            vehicle = Vehicle(json.loads(data.data.decode("utf-8")))

            return vehicle
        else:
            return None


if __name__ == "__main__":
    s = Susanoo()

    print(s.vehicles())
    print(s.people(limit=2, fields={"name", "gender"}))
    print(s.species("74b7f547-1577-4430-806c-c358c8b6bcf5"))
    print(s.film("5fdfb320-2a02-49a7-94ff-5ca418cae602", fields={"id", "title"}))