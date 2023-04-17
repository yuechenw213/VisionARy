using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using UnityEngine.SceneManagement;
using System.IO;

public class LoadPointCloudScript : MonoBehaviour
{
    [SerializeField] public float pointSize;
    [Header("Load Single Object")]
    [SerializeField] public string filePath;

    private Color pointCloudColor;

    public void StartLoad()
    {
        string fileName = Path.GetFileNameWithoutExtension(filePath);
        GameObject newObject = new GameObject(fileName);
        MeshFilter meshFilter = newObject.AddComponent<MeshFilter>();
        MeshRenderer meshRenderer = newObject.AddComponent<MeshRenderer>();
        Material material = new Material(Shader.Find("Unlit/PointCloud"));
        material.color = pointCloudColor;
        meshRenderer.material = material;
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
            // set the material of the mesh renderer to be a point cloud shader
            Material material = new Material(Shader.Find("Unlit/PointCloud"));
            material.color = pointCloudColor;
            meshRenderer.material = material;
            meshFilter.mesh = LoadPLYData(filePath);
        }
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

            int i = 0;
            while ((line = reader.ReadLine()) != null && i < vertexCount)
            {
                string[] tokens = line.Split(' ');
                vertices[i] = new Vector3(float.Parse(tokens[0]), float.Parse(tokens[1]), float.Parse(tokens[2]));

                if (i == 0)
                {
                    pointCloudColor = new Color(float.Parse(tokens[3])/256, float.Parse(tokens[4]) / 256, float.Parse(tokens[5]) / 256);
                   
                }
                i++;
            }

            // set the size of the points in the point cloud
            Vector3[] norms = new Vector3[vertices.Length];
            for (int j = 0; j < norms.Length; j++)
            {
                norms[j] = Vector3.one * pointSize;
            }


            // set the indices of the mesh to be a point for each vertex
            int[] indices = new int[vertices.Length];
            for (int j = 0; j < indices.Length; j++)
            {
                indices[j] = j;
            }

            mesh.vertices = vertices;
            // set the normals of the mesh to be the size of the points
            mesh.normals = norms;
            // set the indices of the mesh
            mesh.SetIndices(indices, MeshTopology.Points, 0);

            //mesh.RecalculateNormals();
            //mesh.RecalculateBounds();

            return mesh;
        }
    }
}
