import getpass
import platform
import socket

class OSDataMixin(object):
    """docstring for OSMixin."""
    def render_data(self):
        """Get the data for the commands"""
        data = super(OSDataMixin, self).render_data()

        data['user'] = getpass.getuser()
        data['system'] =platform.system()
        data['release'] =platform.release()
        data['host'] = socket.gethostbyname(socket.gethostname())

        return data
