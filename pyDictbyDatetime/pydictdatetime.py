from datetime import datetime
from itertools import dropwhile, ifilter

__author__ = 'philippe'

def dateInside(date,start,end):
    return date is None or\
           ((start is None or start <= date)\
            and (end is None or end >= date))






class DictByDatetime(dict):
    #__data__ = dict()



    def has_key(self, key,date = datetime.now()):
        for key in dropwhile(lambda k,startdate,enddate:
            key == k
            and dateInside(date,startdate,enddate),
            super(DictByDatetime, self)
        ):
            return True
        else:
            return False



    def items(self,date=datetime.now()):

        return filter(lambda tk,v: dateInside(date,tk[1],tk[2]), super(DictByDatetime, self).items())


    def itervalues(self,date=datetime.now()):
        return [v for k,v in self.iteritems(date)]


    def iteritems(self, date=datetime.now()):
        return ifilter(lambda (tk,v): dateInside(date,tk[1],tk[2]), super(DictByDatetime, self).iteritems())

    def get(self, key, default=[],date=datetime.now()):
        lst = self.itervalues(date)
        if len(lst) ==0:
            return [default]
        else:
            return lst



    def __eq__(self, y):
        return super(DictByDatetime, self).__eq__(y)

    def __reduce_ex__(self, *args, **kwargs):
        return super(DictByDatetime, self).__reduce_ex__(*args, **kwargs)

    def __hash__(self):
        return super(DictByDatetime, self).__hash__()

    def __getitem__(self, key):
        return list(self.itervalues(date=None))


    def iterkeys(self,date=datetime.now()):
        return (k[0] for k,v in self.iteritems(date))


    def values(self,date=datetime.now()):
        return filter(lambda tk,v: dateInside(date,tk[1],tk[2]), super(DictByDatetime, self).iteritems())

    def __setitem__(self, key, value):
        """
        The key must be a string or a cuple (keystring,startdate) or (keystring,(startdate,enddate))
        keystring must be a basestring
        startdate et enddate must be a datetime or None
        """
        if not isinstance(key,tuple) and not isinstance(key,basestring):
            raise TypeError( DictByDatetime.__setitem__.__doc__, " giving : ",key)
        startdate = enddate = None
        if isinstance(key,tuple):
            if len(key)!=2:
                raise TypeError( DictByDatetime.__setitem__.__doc__, " giving : ",key)
            if isinstance(key[1],tuple):
                if len(key[1])==1 \
                    or (key[1][1] is not None and not isinstance(key[1][1],datetime) \
                        and key[1][0] is not None and not isinstance(key[1][0],datetime)):
                        raise TypeError( DictByDatetime.__setitem__.__doc__, " giving : ",key)
                enddate= key[1][1]
                startdate= key[1][0]
            else:
                if key[1] is not None and not isinstance(key[1],datetime):
                    raise TypeError( DictByDatetime.__setitem__.__doc__, " giving : ",key)
                startdate= key[1]
        if not isinstance(key[0],basestring):
            raise TypeError( DictByDatetime.__setitem__.__doc__, " giving : ",key, type(key[0]))
        keystring= key[0]
        super(DictByDatetime, self).__setitem__((key,startdate,enddate), value)

    def pop(self, key, default=None):
        return super(DictByDatetime, self).pop(key, default)

    def __contains__(self, k):
        return self.has_key(k,date=None)
    #
    #def update(self, other=None, **kwargs):
    #    super(DictByDatetime, self).update(other, **kwargs)