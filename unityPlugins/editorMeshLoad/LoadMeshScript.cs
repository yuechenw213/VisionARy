using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using UnityEngine.SceneManagement;
using System.IO;


public class LoadMeshScript : MonoBehaviour
{
    [Header("Load Single Object")]
    [SerializeField] public string filePath;

    public void StartLoad()
    {
        string fileName = Path.GetFileNameWithoutExtension(filePath);
        GameObject newObject = new GameObject(fileName);
        MeshFilter meshFilter = newObject.AddComponent<MeshFilter>();
        MeshRenderer meshRenderer = newObject.AddComponent<MeshRenderer>();
        meshRenderer.sharedMaterial = new Material(Shader.Find("Standard"));
        meshFilter.mesh = LoadPLYData(filePath);

    }

    [Header("Load Object Folder")]
    [SerializeField] public string folderPath;

    public void StartLoadFolder()
    {
        string[] filePaths = Directory.GetFiles(folderPath);

        foreach (string filePath in filePaths)
        {
            Debug.Log(filePath);
            string fileName = Path.GetFileNameWithoutExtension(filePath);
            GameObject newObject = new GameObject(fileName);
            MeshFilter meshFilter = newObject.AddComponent<MeshFilter>();
            MeshRenderer meshRenderer = newObject.AddComponent<MeshRenderer>();
            meshRenderer.sharedMaterial = new Material(Shader.Find("Standard"));
            meshFilter.mesh = LoadPLYData(filePath);
        }
        //string fileName = Path.GetFileNameWithoutExtension(filePath);
        //GameObject newObject = new GameObject(fileName);
        //MeshFilter meshFilter = newObject.AddComponent<MeshFilter>();
        //MeshRenderer meshRenderer = newObject.AddComponent<MeshRenderer>();
        //meshRenderer.sharedMaterial = new Material(Shader.Find("Standard"));
        //meshFilter.mesh = LoadPLYData(filePath);

    }


    public Mesh LoadPLYData(string filePath)
    {
        using (StreamReader reader = new StreamReader(filePath))
        {
            string line = null;
            int vertexCount = 0, faceCount = 0;
            while ((line = reader.ReadLine()) != null && !line.Contains("end_header"))
            {
                if (line.StartsWith("element vertex"))
                {
                    int.TryParse(line.Split(' ')[2], out vertexCount);
                }
                else if (line.StartsWith("element face"))
                {
                    int.TryParse(line.Split(' ')[2], out faceCount);
                }
            }

            Mesh mesh = new Mesh();
            Vector3[] vertices = new Vector3[vertexCount];
            Color[] colors = new Color[vertexCount];
            int[] triangles = new int[faceCount * 3];

            int i = 0;
            while ((line = reader.ReadLine()) != null && i < vertexCount)
            {
                string[] tokens = line.Split(' ');
                vertices[i] = new Vector3(float.Parse(tokens[0]), float.Parse(tokens[1]), float.Parse(tokens[2]));
                colors[i] = new Color(float.Parse(tokens[3]), float.Parse(tokens[4]), float.Parse(tokens[5]));

                i++;
            }

            i = 0;
            while ((line = reader.ReadLine()) != null && i < faceCount)
            {
                string[] tokens = line.Split(' ');
                triangles[i * 3] = int.Parse(tokens[1]);
                triangles[i * 3 + 1] = int.Parse(tokens[2]);
                triangles[i * 3 + 2] = int.Parse(tokens[3]);

                i++;
            }

            mesh.vertices = vertices;
            mesh.colors = colors;
            mesh.triangles = triangles;
            mesh.RecalculateNormals();
            mesh.RecalculateBounds();

            return mesh;
        }
    }

}
