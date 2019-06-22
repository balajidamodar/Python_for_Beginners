"""3) There are TVs. A TV has a name and channel that is being displayed. You can increment/decrement channel.
 You can change the channel to a given number as well. You can ask the TV to display. When a TV is asked to display,
 it will print the channel num, the volume.TV has volume (int).
You have to switch on the TV first before you can operate the channels or increase or decrease the volume. Design and test TV working."""

class Tv():
    ''' tv class to test the working '''
    def __init__(self,name):
        '''initialize the instance var on object creation'''
        self.name = name
        self.channel = 50
        self.volume = 10
        control = str(input("do you want to switch on the tv, yes or no ?"))
        if control.upper() == "YES":
            self.tv_switch_on()
        else:
            print("tv is not switched on")

    def __str__(self):
        return "this tv is {} displaying channel {} has volume {} ".format(self.name,self.channel,self.volume)

    def tv_switch_on(self):
        print(" %s tv switched on" %(self.name))

    def tv_display(self):
        print("displaying channel {} current volume is {}".format(self.channel,self.volume))

    def channel_change(self,ch_no:"int")->"None":
        self.channel = ch_no
        chan_dic ={
            1:"sports",
            2:"pogo",
            3:"musics",
            4:"sony",
            5:"Fashion tv",
            6:"History tv",
            7:"cartoon",
            8:"tv9",
            9:"CNBC",
            10:"TIMES NOW"
        }
        if self.channel < 0 or self.channel >10:
            print("opted channel not available,contact cable operator to activate")
        else:
            print("channel changed to {}, you are watching {} ".format(self.channel,chan_dic[self.channel]))

    def increment_vol(self,mode:"str",vol:"int")->"None":
        inc = "increment"
        if inc == mode :
            self.volume += vol
            print("volume incremented to %s" %(self.volume))
        else:
            self.volume -= vol
            print("volume decremented to %s" % (self.volume))

tv1 = Tv("onida")
print(tv1)
#tv1.tv_switch_on()
tv1.tv_display()
tv1.increment_vol("increment",10)
tv1.increment_vol("decrement",10)
tv1.channel_change(20)
tv1.channel_change(10)
print(tv1)