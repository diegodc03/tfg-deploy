
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';

import React from 'react';
import CardActionArea from '@mui/material/CardActionArea';
import { useNavigate } from 'react-router-dom';


type CardShowProps = {
    title: string;
    text: string;
    image: string;
    navigateElement?: string; // Prop opcional para la navegación
  };


const CardShow: React.FC<CardShowProps> = ({ title, text, image, navigateElement }) => {

    const navigate = useNavigate();

    const handleChangeScoresView = () => {

        if (navigateElement) {
            console.log("navegando a: ", navigateElement);
            navigate(`${navigateElement}`);
        }

    };


    return (
        <Card
        sx={{
            width: 220,
            height: 250,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            borderRadius: 3,
        }}
        >          
        <CardActionArea  sx={{ width: '100%' }}>
            
                <CardMedia
                        component="img"
                        image={image}
                        alt={title}
                        onClick={() => {handleChangeScoresView()}}
                        sx={{
                            width: 110,
                            height: 100, // Igual que el ancho del card
                            objectFit: 'cover', // Recorta para mantener proporción sin deformar
                            borderRadius: 2, // Bordes redondeados
                            marginTop: 1, // Espacio superior
                            marginBottom: 1, // Espacio inferior
                            // poner en e centro
                            display: 'flex',
                            justifyContent: 'center',
                            alignItems: 'center',
                    
                            }}
                    />
                <CardContent>
                    <Typography gutterBottom variant="h5" component="div" fontWeight="bold">
                        {title}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        {text}
                    </Typography>

                </CardContent>


          
          </CardActionArea>
        </Card>
      );
  };

export default CardShow;