# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

from collecting_society_portal.resources import (
    ResourceBase,
    BackendResource
)


class MusicfanResource(ResourceBase):
    __name__ = "musicfan"
    __parent__ = BackendResource
    __children__ = {}
    __acl__ = []


class MusicianResource(ResourceBase):
    __name__ = "musician"
    __parent__ = BackendResource
    __children__ = {}
    __acl__ = []


class MusicfanDummyResource(ResourceBase):
    __name__ = "musicfan"
    __parent__ = MusicfanResource


class ClientResource(ResourceBase):
    __name__ = "clients"
    __parent__ = MusicfanResource
    __children__ = {}
    __registry__ = {}
    __acl__ = []


class UtilisationIMPMusicfanResource(ResourceBase):
    __name__ = "utilisations"
    __parent__ = MusicfanResource
    __children__ = {}
    __registry__ = {}
    __acl__ = []


class UtilisationIMPMusicianResource(ResourceBase):
    __name__ = "utilisations"
    __parent__ = MusicianResource
    __children__ = {}
    __registry__ = {}
    __acl__ = []
