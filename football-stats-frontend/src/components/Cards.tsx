
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
            height: 270,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            borderRadius: 3,
     
        }}
        >          
            <CardActionArea  sx={{ width: '100%' }} onClick={() => {handleChangeScoresView()}}>
            
                <CardMedia
                        component="img"
                        image={image}
                        alt={title}
                        sx={{
                                width: 110,
                                height: 100,
                                borderRadius: 2,
                                marginTop: 2,
                                marginBottom: 1,
                                display: 'block',
                                marginLeft: 'auto',
                                marginRight: 'auto',
                            }}
                    />
                <CardContent>
                    <Typography gutterBottom variant="h6" component="div" fontWeight="bold" sx={{ textAlign: 'center' }}>
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