import pygame,sys
pygame.init()
clock = pygame.time.Clock()
width=500
height=500
screen= pygame.display.set_mode((width,height)) 
pygame.display.set_caption('Mein Editor')
font = pygame.font.SysFont('Arial',20) 

#####

speichern_text="speichern"
öffnen_text="öffnen"
user_text= 'input'
title_text= 'file'
data_text= 'Datei als:'


speichern_rect=pygame.Rect(400,0,100,30)
öffnen_rect=pygame.Rect(0,0,100,30)
input_rect = pygame.Rect(0,30,500,470)
title_rect = pygame.Rect(200,2,150,26)

#####

active=False
active2=False
topdown_bool=False
color="white"
farbe="white"


####
def save(text,title_text):
	with open(title_text,"w") as file:
		file.write(text)
      
def öffnen(eingabe):
	with open(eingabe,"r") as file:
		return file.read()
      
def speichere_liste(title_text):
   aktuelle_Liste=öffne_liste()
   if title_text not in aktuelle_Liste:
	   with open("config.txt","a") as file:
		   file.writelines(title_text +"\n")

def öffne_liste():
	with open("config.txt","r") as file:
		return [line.strip() for line in file.readlines()]

topdown_menu=öffne_liste()
############################
while True:    
   for events in pygame.event.get():
      if events.type==pygame.QUIT:
         pygame.quit()
         sys.exit()
              
      elif events.type==pygame.MOUSEBUTTONDOWN:
         if speichern_rect.collidepoint(events.pos):
             save(user_text,title_text)
             topdown_menu.append(title_text)
             speichere_liste(title_text)

         if öffnen_rect.collidepoint(events.pos):
          
            topdown_bool=not topdown_bool
            active=False

         

         if input_rect.collidepoint(events.pos) and topdown_bool==False:
            active = True
         else:
           active=False
         if title_rect.collidepoint(events.pos):
            active2 = True
         else:
           active2=False
         


      elif events.type == pygame.KEYDOWN:


         if active == True:
            if events.key == pygame.K_BACKSPACE:
               user_text = user_text[:-1]
            elif events.key == pygame.K_RETURN:
               user_text+='\n'
            else:
               user_text+=events.unicode
         if active2 == True:
            if events.key == pygame.K_BACKSPACE:
              title_text = title_text[:-1]
            
            else:
               title_text+=events.unicode

   

   screen.fill((30,30,30))
   if active:
      color="green"
   else:
      color="grey"
   if active2:
      color2="green"
   else:
      color2="grey"
   
   pygame.draw.rect(screen,color,input_rect,2)
   pygame.draw.rect(screen,(65,65,66),speichern_rect)
   pygame.draw.rect(screen,(65,65,66),öffnen_rect)
   pygame.draw.rect(screen,color2,title_rect,2)

   
   data_surface = font.render(data_text,True,(250,250,250))
   screen.blit(data_surface,(title_rect.x - 80, title_rect.y +3))

   title_surface = font.render(title_text,True,(250,250,250))
   screen.blit(title_surface,(title_rect.x + 5, title_rect.y +3))

   speichern_surface = font.render(speichern_text,True,(255,255,255))
   screen.blit(speichern_surface,(speichern_rect.x + 10, speichern_rect.y +5))

   öffnen_surface = font.render(öffnen_text,True,(255,255,255))
   screen.blit(öffnen_surface,(öffnen_rect.x + 25, öffnen_rect.y +5))
   

   i=0
   inside= False
   x_offset=input_rect.x+5
   y_offset=input_rect.y+5
   while i < len(user_text):
         if user_text[i:i+1] =='\n':

                x_offset=input_rect.x+5
                y_offset+=20
                i+=1
         elif  user_text[i:i+5] =='print' or user_text[i:i+1] =='(' or user_text[i:i+1] ==')' :
            farbe='yellow'
            if user_text[i:i+1] =='(':
               ix = font.render('(',True,farbe)
               screen.blit(ix,(x_offset, y_offset))
               x_offset+=ix.get_width()
               inside=True
               i+=1
            if user_text[i:i+1]==')':
               ix = font.render(')',True,farbe)
               screen.blit(ix,(x_offset, y_offset))
               x_offset+=ix.get_width()
               inside=False
               i+=1
            if user_text[i:i+5] =='print':
                ix = font.render('print',True,farbe)
                screen.blit(ix,(x_offset, y_offset))
                x_offset+=ix.get_width()
                inside=False
                i+=5
            #continue
            
        
             
         else:
            farbe='white'
            ix = font.render(user_text[i],True,farbe)
            screen.blit(ix,(x_offset, y_offset))
            x_offset+=ix.get_width()
            inside=False
            i+=1
             

   if topdown_bool:
      abstand=10
      topdown_rect=pygame.Rect(0,30,100,200)
      pygame.draw.rect(screen,(65,65,66),topdown_rect)
     
      for i in topdown_menu:
         abstand+=30
         rect=pygame.Rect(0,0+abstand,100,30)
         pygame.draw.rect(screen,(65,65,66),rect)
         
         topdown_surface = font.render(i,True,(255,255,255))
         screen.blit(topdown_surface,(rect.x+15,rect.y))
         
         if events.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(events.pos):
            user_text = öffnen(i)  
            topdown_bool = False  

   pygame.display.flip()
   clock.tick(60)